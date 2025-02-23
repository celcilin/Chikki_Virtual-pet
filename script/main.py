from flask import Flask, request, jsonify, send_file
from flask_socketio import SocketIO
import asyncio
import speech_recognition as sr
import edge_tts
import os
from ollama import AsyncClient

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Initialize speech recognizer
recognizer = sr.Recognizer()

@app.route('/')
def index():
    return "Chikki AI Server Running!"

# 🔹 **Speech Recognition (STT) - Listens to User**
@app.route('/api/listen', methods=['GET'])
def listen_and_transcribe():
    try:
        with sr.Microphone() as source:
            print("🎤 Listening for user input...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        text = recognizer.recognize_google(audio)
        print(f"🗣️ You: {text}")

        return jsonify({"text": text})

    except sr.UnknownValueError:
        return jsonify({"error": "I couldn't understand that."})
    except sr.RequestError:
        return jsonify({"error": "Speech service is unavailable."})

# 🔹 **AI Chat Response using Ollama LLM**
@app.route('/api/llm', methods=['POST'])
async def generate_text():
    try:
        data = request.json
        input_text = data.get("text", "")

        if not input_text:
            return jsonify({"error": "No text provided"}), 400

        message = {'role': 'user', 'content': input_text}
        response = await AsyncClient().chat(model="chikki_1.2:latest", messages=[message])

        reply = response.message.content
        print(f"🤖 Chikki: {reply}")

        data = await generate_voice(reply)
        print(data)

        return jsonify({"input": input_text, "generated_text": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 🔹 **Text-to-Speech (TTS) - AI Voice**
# @app.route('/api/tts', methods=['POST'])
from pydub import AudioSegment

async def generate_voice(input_text):
    try:
        if not input_text:
            return {"error": "No text provided"}, 400

        mp3_path = "output_voice.mp3"  # Edge TTS saves as MP3
        wav_path = "output_voice.wav"  # Converted WAV for Godot

        # Generate TTS audio in MP3 format
        communicate = edge_tts.Communicate(input_text, voice="en-US-AriaNeural", rate="+0%")
        await communicate.save(mp3_path)

        # Convert MP3 to WAV using pydub
        sound = AudioSegment.from_file(mp3_path, format="mp3")
        sound.export(wav_path, format="wav")

        return send_file(wav_path, as_attachment=True)

    except Exception as e:
        return {"error": str(e)}, 500


# 🔹 **WebSocket Handler for Godot**
@socketio.on("listen")
def handle_listen():
    user_input = listen_and_transcribe().get_json().get("text", "")
    if user_input:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        response = loop.run_until_complete(generate_text().get_json().get("generated_text", ""))
        
        socketio.emit("response", {"text": response})

        # Convert AI response to speech
        loop.run_until_complete(generate_voice().get_json())

if __name__ == '__main__':
    socketio.run(app, port=5000, allow_unsafe_werkzeug=True,debug=True)
