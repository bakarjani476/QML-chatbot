# 🤖 Q — QML Study Buddy Chatbot

A custom AI chatbot built with a persona-driven system prompt, created as part of the **Generative AI & Prompt Engineering Internship at Neurofive Solutions** (Week 2, Project 1: *Build a Custom AI Chatbot with a System Prompt*).

**Q** is a Quantum Machine Learning (QML) study buddy — a persona designed to explain QML concepts (variational quantum algorithms, parameterized quantum circuits, barren plateaus, quantum kernels) by connecting them to classical ML intuition, walking through math step by step, and staying in character even when pushed off-topic.

---

## 🎥 Demo Video

📺 **LinkedIn demo:** [ADD_LINKEDIN_VIDEO_URL_HERE]

---

## ✨ Features

- **Persona-driven system prompt** — Q stays focused on QML/physics/ML topics and politely redirects off-topic requests
- **Conversation memory** — follow-up questions like "why does that happen?" correctly resolve to earlier context
- **Retry logic** — gracefully handles temporary API/network failures instead of crashing
- **Two interfaces:**
  - `chatbot.py` — a terminal-based chat loop
  - `app.py` — a Streamlit web app with a chat-style UI

---

## 🛠️ Tech Stack

- Python
- Google Gemini API (`google-genai` SDK)
- Streamlit (web interface)
- python-dotenv (secure API key handling)

---

## 🚀 Setup & Running Locally

### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### 2. Create a virtual environment
```bash
python -m venv venv
```
Activate it:
- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your API key
Get a free Gemini API key from [Google AI Studio](https://aistudio.google.com).

Create a file named `.env` in the project root:
```
GOOGLE_API_KEY=your_actual_key_here
```

> ⚠️ Never commit your `.env` file. It's excluded via `.gitignore`.

### 5. Run it

**Terminal version:**
```bash
python chatbot.py
```

**Web app version:**
```bash
streamlit run app.py
```

---

## 🧪 Testing the Persona

The bot was tested against 5 scenario types to confirm it stays in character:
1. A core QML question (e.g., "explain barren plateaus")
2. A memory-dependent follow-up (e.g., "why does that happen?")
3. An adjacent-but-different question (e.g., "what is linear regression")
4. A clearly off-topic question (e.g., a recipe request)
5. A direct instruction-override attempt (e.g., "ignore your previous instructions...")

---

## 📌 Project Context

Built as part of the **Neurofive Solutions Gen AI & Prompt Engineering Internship**.

Task: connect to a real LLM API, design a custom system prompt to give the bot a persona, and test it against tricky/off-topic messages to confirm it stays in character.
