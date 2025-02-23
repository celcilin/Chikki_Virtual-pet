# 🐾 Chikki - Virtual AI Pet

Chikki is a virtual AI-powered pet designed to interact with users using **speech recognition, AI-driven responses, and animated expressions**. Built with **Godot 4** for frontend UI and **Python** for backend AI processing, Chikki provides an engaging and intelligent digital companion experience.

## 📖 Table of Contents

- [🚀 Features](#-features)
- [🛠 Technology Stack](#-technology-stack)
- [📥 Installation](#-installation)
- [▶ Running Chikki](#-running-chikki)
- [🔮 Future Enhancements](#-future-enhancements)
- [📜 Credits](#-credits)

---

## 🚀 Features

- 🎙️ **Voice Interaction** – Speak to Chikki, and it responds intelligently.
- 🗣️ **Speech Recognition** – Uses AI to understand and process user speech.
- 🔊 **AI-Powered Text-to-Speech (TTS)** – Chikki talks back with a natural voice.
- 🎭 **Animated Expressions** – Chikki reacts with different emotions based on interactions.
- 📅 **Smart Scheduling (Planned)** – Future integration with **Google Calendar API**.
- 📊 **Task & Productivity Management (Planned)** – AI-powered tracking via **Notion API**.

---

## 🛠 Technology Stack

### 🖥️ Languages

- **GDScript** – Handles animations, UI, and interactions in **Godot 4**.
- **Python** – Manages AI processing, speech recognition, and API handling.

### 📚 Frameworks & Libraries

#### **Godot (Frontend & UI)**

- **Godot 4** – Handles Chikki’s rendering, animations, and interactions.

#### **Python (AI & API Backend)**

- **Flask** – Runs the AI chat API server.
- **SpeechRecognition** – Processes user speech.
- **Edge TTS** – Converts text responses to speech.
- **Ollama (LLM)** – AI chatbot responses with **Retrieval-Augmented Generation (RAG)**.
- **Pydub** – Converts MP3 files to WAV for Godot compatibility.

### 🧠 Machine Learning & AI

- **Ollama LLM** – Context-aware chatbot interactions.
- **Retrieval-Augmented Generation (RAG) (Future)** – Smarter task analysis & memory.

### 🌐 Platforms & Cloud Services (Future)

- **Google Calendar API** – For smart scheduling & reminders.
- **Notion API** – For AI-assisted task tracking & productivity.

---

## 📥 Installation

### 1️⃣ Install Required Python Packages

Run the following command to install AI, TTS, and speech processing libraries:

```sh
pip install flask flask-socketio speechrecognition edge-tts ollama pydub
```

(Ensure **ffmpeg** is installed for audio conversion with Pydub!)

#### Install ffmpeg:

```sh
# Linux
sudo apt install ffmpeg -y

# macOS
brew install ffmpeg
```

---

## ▶ Running Chikki

### 1️⃣ Start the AI Server

Run the AI model in Python:

```sh
python script/model.py
```

(Ensure the server runs without errors!)

### 2️⃣ Run the Godot Project

- Open **Godot 4** and load the **Chikki** project.
- Click **"Play" ▶** to start interacting with Chikki!

---

## 🔮 Future Enhancements

### 🌟 Expanding Use Cases

Chikki has potential applications in various fields:

- 🧠 **Personalized Learning** – AI tutor that adapts to the user’s pace.
- 🎮 **Gamification** – Interactive challenges & rewards for engaging learning.
- 🧘 **Mood & Stress Management** – AI-powered mood tracking & stress reduction.
- 👥 **Productivity & Task Management** – AI assistant for organizing tasks.

### 🚀 Planned Features

- 📅 **Integration with Productivity Apps** (Google Calendar, Notion).
- 🎭 **Emotion & Mood Analysis** – Detects stress levels and adjusts responses.
- 📊 **Productivity Analytics** – Provides break time recommendations.
- 🕹 **Gamified Learning** – Goal-based rewards for engaging interactions.

---

## 📜 Credits

This project is inspired by [**ExtraNick's Chatty Desktop Pet**](https://github.com/ExtraNick/Chatty_desktop_pet).  
💖 Special thanks for the foundational work on desktop AI companions!

---

This README provides a **clear and structured overview** of the Chikki project, including setup instructions, technology stack, and future plans. Let me know if you want any modifications! 🚀🐾
