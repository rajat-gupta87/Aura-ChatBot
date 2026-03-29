"""
app.py — Flask backend for AI Chatbot using Groq API
"""

from flask import Flask, request, jsonify, render_template
from groq import Groq
import time, os
from dotenv import load_dotenv

load_dotenv()

# ── App Setup ─────────────────────────────────────────────
app = Flask(__name__)

# Initialize Groq client
client = Groq(
    api_key = os.getenv("API_KEY")
)

# ── Routes ─────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    try:

        data = request.get_json(force=True)

        user_message = data.get("message", "").strip()
        client_history = data.get("history", [])

        if not user_message:
            return jsonify({"error": "Empty message"}), 400

        # Build conversation history
        messages = []

        for entry in client_history:
            role = entry.get("role")
            content = entry.get("content")

            if role in ["user", "assistant"] and content:
                messages.append({
                    "role": role,
                    "content": content
                })

        # Add latest user message
        messages.append({
            "role": "user",
            "content": user_message
        })

        # Call Groq AI
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.7,
            max_tokens=1024
        )

        reply_text = response.choices[0].message.content

        return jsonify({
            "reply": reply_text,
            "timestamp": int(time.time() * 1000)
        })

    except Exception as exc:

        print("SERVER ERROR:", exc)

        return jsonify({
            "error": str(exc)
        }), 500


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


# ── Entry Point ───────────────────────────────────────────

if __name__ == "__main__":
    app.run(debug=True, port=5000)