# Aura — AI Chatbot

A modern, AI-powered chatbot web application built with Flask and vanilla JavaScript, powered by Groq for ultra-fast AI responses.
Designed with a focus on performance, responsiveness, and a clean user experience.

---

## Features

*  **Real-time AI responses** using Groq LLMs
*  **Ultra-fast inference** powered by Groq API
*  **Voice input** (Speech-to-Text via Web Speech API)
*  **Voice output** (Text-to-Speech responses)
*  **Dark / Light mode** with persistent user preference
*  **Markdown rendering** (code blocks, lists, formatting)
*  **Chat history storage** using browser localStorage
*  **Animated UI** (typing indicator, pulse avatar, orb effects)
*  **Fully responsive design** (mobile, tablet, desktop)
*  **Error handling** (API failures, rate limits, network issues)

---

## Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS, JavaScript
* **AI API:** Groq (LLMs like LLaMA / Mixtral)
* **Browser APIs:** Web Speech API (STT & TTS)

---

## Project Structure

```id="38lky2"
Aura-ChatBot/
│── app.py
│── requirements.txt
│── templates/
│   └── index.html
│── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── app.js
```

---

## Quick Start

### 1️ Clone the repository

```bash id="e3s6aq"
git clone https://github.com/your-username/Aura-ChatBot.git
cd Aura-ChatBot
```

---

### 2️ Install dependencies

```bash id="m2i8i7"
pip install -r requirements.txt
```

---

### 3️ Set your Groq API key

#### Option A — Environment Variable (Recommended)

**Windows (PowerShell):**

```powershell id="u5h3vk"
$env:GROQ_API_KEY="your_api_key_here"
```

**macOS / Linux:**

```bash id="aq7n0t"
export GROQ_API_KEY="your_api_key_here"
```

---

#### Option B — Direct in Code *(Not recommended for production)*

Update inside `app.py`:

```python id="uwx6sd"
api_key = "YOUR_API_KEY_HERE"
```

---> Get your API key from: https://console.groq.com

---

### 4️ Run the application

```bash id="08pdn9"
python app.py
```

---

### 5️ Open in browser

```id="p5szav"
http://127.0.0.1:5000
```

---

## Voice Interaction

* Click mic🎙️ to start recording
* Click again or wait for auto-stop
* Speech is automatically converted to text
* AI response is spoken back using Text-to-Speech

⚠️ Best supported on Chrome / Edge browsers

---

## Configuration

| Variable       | Default  | Description              |
| -------------- | -------- | ------------------------ |
| `GROQ_API_KEY` | Required | Your Groq API key        |
| `PORT`         | 5000     | Change in app.py         |
| `DEBUG`        | True     | Set False for production |

---

## Deployment

You can deploy this project on:

* Render (recommended for Flask apps)
* Railway
* VPS (Gunicorn + Nginx)

---

## Notes

* Chat history is stored in **browser localStorage**
* No server-side session storage is used
* Fast responses powered by Groq inference engine
* Disable `debug=True` in production

---

## Author

**Rajat Gupta**
GitHub: https://github.com/rajat-gupta87

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!


## Supported Browsers

| Feature         | Chrome | Edge |   Firefox   | Safari  |
|-----------------|--------|------|-------------|---------|
| Chat            | ✅     | ✅   | ✅         | ✅     |
| Voice Input     | ✅     | ✅   | ⚠️ partial | ❌     |
| Voice Output    | ✅     | ✅   | ✅         | ✅     |

---

## Notes

- Chat history is stored in **browser localStorage** — it persists across page refreshes but is per-browser and per-origin.
- The server keeps no conversation state between restarts; history is sent from the client on each request.
- For production deployment, disable `debug=True` and serve with Gunicorn behind a reverse proxy (Nginx/Caddy).
