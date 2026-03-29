# Aura — AI Chatbot

A fully responsive AI chatbot powered by Anthropic Claude, built with Flask + vanilla JS.

---

## Features

- **Real-time AI answers** via Anthropic Claude (claude-sonnet)
- **Voice input** using the Web Speech API (Speech-to-Text)
- **Voice output** using the Web Speech Synthesis API (Text-to-Speech)
- **Dark / Light mode** toggle with persistence
- **Markdown rendering** for code blocks, lists, and bold text
- **Chat history** saved in browser localStorage
- **Animated UI** — typing indicator, pulse avatar, orb background
- **Fully responsive** — mobile, tablet, and desktop
- **Error handling** for API failures, rate limits, and network issues

---

## Project Structure

```
chatbot/
├── app.py                  # Flask backend
├── requirements.txt
├── templates/
│   └── index.html          # Main UI template
└── static/
    ├── css/
    │   └── style.css       # All styles + theme tokens
    └── js/
        └── app.js          # Frontend logic
```

---

## Quick Start

### 1. Install Python dependencies

```bash
cd chatbot
pip install -r requirements.txt
```

### 2. Set your Anthropic API key

**Option A — environment variable (recommended)**

macOS / Linux:
```bash
export ANTHROPIC_API_KEY=sk-ant-...
```

Windows (PowerShell):
```powershell
$env:ANTHROPIC_API_KEY = "sk-ant-..."
```

**Option B — hard-code in `app.py`** *(not for production)*

Open `app.py` and replace `"YOUR_API_KEY_HERE"` with your actual key.

Get a key at https://console.anthropic.com

### 3. Run the server

```bash
python app.py
```

### 4. Open in your browser

```
http://localhost:5000
```

---

## Voice Interaction

- **Microphone button** → click to start recording, click again to stop (or wait for auto-stop)
- The transcript is auto-sent after recording ends
- **Text-to-speech** plays automatically after each AI response
- Voice features require a modern browser (Chrome/Edge recommended)

---

## Configuration

| Variable              | Default                  | Description                  |
|-----------------------|--------------------------|------------------------------|
| `ANTHROPIC_API_KEY`   | `YOUR_API_KEY_HERE`      | Your Anthropic API key       |
| Flask `port`          | `5000`                   | Change in `app.py`           |
| Flask `debug`         | `True`                   | Set `False` for production   |

---

## Supported Browsers

| Feature          | Chrome | Edge | Firefox | Safari |
|-----------------|--------|------|---------|--------|
| Chat            | ✅     | ✅   | ✅      | ✅     |
| Voice Input     | ✅     | ✅   | ⚠️ partial | ❌  |
| Voice Output    | ✅     | ✅   | ✅      | ✅     |

---

## Notes

- Chat history is stored in **browser localStorage** — it persists across page refreshes but is per-browser and per-origin.
- The server keeps no conversation state between restarts; history is sent from the client on each request.
- For production deployment, disable `debug=True` and serve with Gunicorn behind a reverse proxy (Nginx/Caddy).
