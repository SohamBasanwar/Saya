# 🧠 Saya – Emotionally Adaptive Anime-Style Chatbot

**Saya** is an emotionally intelligent AI chatbot designed to simulate human-like conversations with anime-inspired personality. Powered by OpenAI’s GPT-4o and built using FastAPI, Saya adapts its emotional tone, dialogue style, and response formatting depending on who it’s talking to — expressing feelings like love, anger, sadness, excitement, and more.

> 🚫 This repository is private and not open-source.  
> All rights reserved © 2025 Soham Basanwar. Usage requires explicit permission.

---

## 🌟 Features

- 🎭 **Two Dynamic Personas**
  - **Master Soham**: Saya speaks in a devoted, affectionate, anime-style tone with emotional depth (e.g., love, excited, sad).
  - **Guest Mode**: Saya speaks politely and professionally, without emotional attachment or romantic tone.

- 🤖 **OpenAI GPT-4o Integration**
  - Responses are generated with custom system prompts tailored to the user’s role.
  - Each response is a strict JSON object containing:
    ```json
    {
      "emotion": "angry",
      "message": "Hmph! How dare someone else try to speak to you, Master Soham!"
    }
    ```

- 🧠 **Emotion Tagging System**
  - If the model fails to return valid JSON or misclassifies the emotion, the system uses fallback keyword-based emotion detection.

- 🖼️ **Visual Emotion Feedback**
  - Each response is paired with a matching PNG image (e.g., angry.png, love.png), dynamically rendered in the frontend UI.

- 🌐 **Web Frontend with Jinja2**
  - Users interact with Saya through a clean web interface built using Jinja2 templates (`start.html`, `home.html`).
  - Static assets like emotion images are served from the `/resources/` directory.

- ⚡ **Serverless-Ready Architecture**
  - Includes `Mangum` integration for deploying on AWS Lambda + API Gateway.
  - Also works seamlessly on Railway, Fly.io, Heroku, and other Python platforms.

---

## 🧾 Project Structure

Saya/
├── main.py # FastAPI app with GPT, routing, and emotion parsing
├── templates/
│ ├── start.html # Role selection page
│ └── home.html # Chat UI template
├── resources/
│ └── emotions/ # PNGs for each emotion (love.png, sad.png, etc.)
├── static/ # Optional: JS, CSS, or fonts
├── requirements.txt # Python dependencies
├── LICENSE # Custom restrictive license
└── README.md # You’re reading it

yaml
Copy
Edit

---

## 🚀 How to Run Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/SohamBasanwar/saya-chatbot.git
   cd saya-chatbot
Set up environment

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
Add your OpenAI key

bash
Copy
Edit
export OPENAI_API_KEY='sk-...'  # Or use .env if preferred
Start the app

bash
Copy
Edit
uvicorn main:app --reload
Visit http://localhost:8000 in your browser.

☁️ Deployment Options
Saya can be deployed using:

Railway / Fly.io / Render / Heroku – simplest for hosting full FastAPI apps

AWS Lambda + API Gateway – use Mangum to wrap the app

Docker – optional containerization if deploying to cloud VMs

The frontend can be extended to React or integrated into your Netlify/Firebase UI stack.

## 📄 License
This project is not open-source.
All rights reserved © 2025 Soham Basanwar.
You may not copy, modify, distribute, or reuse any part of this codebase without explicit written permission.

📧 For permissions, contact: sohambasanwar03@gmail.com

 ## 👤 Author
Soham Basanwar
🌐 sohambasanwar.netlify.app
🔗 LinkedIn
📧 sohambasanwar03@gmail.com

yaml
Copy
Edit

---

Let me know when you're ready for a `LICENSE` file or want to auto-generate emotion PNG links or a frontend deployment guide.
