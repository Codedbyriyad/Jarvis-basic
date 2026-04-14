# 🤖 Jarvis — AI Voice Assistant

A voice-controlled AI assistant built with Python, inspired by Iron Man's J.A.R.V.I.S. Responds to voice commands with a British accent using text-to-speech.

---

## ✨ Features

- 🎙️ Wake word detection — say **"Jarvis"** to activate
- 🔊 British accent text-to-speech responses
- 🌐 Open websites via voice (Google, YouTube, Facebook)
- 🕐 Real-time time reporting
- 🔇 Background noise calibration for accuracy
- 🇧🇩 Supports South Asian English accent recognition (`en-IN`)

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat&logo=python)
![SpeechRecognition](https://img.shields.io/badge/SpeechRecognition-3.10-green?style=flat)
![pyttsx3](https://img.shields.io/badge/pyttsx3-TTS-orange?style=flat)

| Library | Purpose |
|--------|---------|
| `speech_recognition` | Voice input & wake word detection |
| `pyttsx3` | Offline text-to-speech (British voice) |
| `webbrowser` | Open URLs via voice command |
| `datetime` | Real-time clock responses |

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/Codedbyriyad/jarvis-assistant.git
cd jarvis-assistant

# Install dependencies
pip install speechrecognition pyttsx3 pyaudio
```

> **Windows users:** If `pyaudio` fails, install via:
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```

---

## 🚀 Usage

```bash
python jarvis.py
```

Then say **"Jarvis"** — wait for the response, then give a command.

### 🗣️ Supported Commands

| Voice Command | Action |
|--------------|--------|
| `"Hello"` | Greeting response |
| `"What time is it"` | Current time |
| `"Open Google"` | Opens google.com |
| `"Open YouTube"` | Opens youtube.com |
| `"Open Facebook"` | Opens facebook.com |
| `"Stop"` / `"Exit"` | Shuts down Jarvis |

---

## 📁 Project Structure

```
jarvis-assistant/
├── jarvis.py       # Main assistant script
└── README.md       # Project documentation
```

---

## 🔮 Planned Features

- [ ] ChatGPT / Gemini API integration
- [ ] Spotify & music control
- [ ] System controls (volume, shutdown)
- [ ] Custom wake word training
- [ ] GUI dashboard

---

## 👨‍💻 Author

**MD Kaysar Mahmud (Riyad)**  
CSE Undergraduate @ RUET  
GitHub: [@Codedbyriyad](https://github.com/Codedbyriyad)

---

> *"Sometimes you gotta run before you can walk."* — Tony Stark
