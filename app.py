import os
import time
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.environ.get('GOOGLE_API_KEY')
client = genai.Client(api_key = api_key)

SYSTEM_PROMPT = """
You are Q, a friendly and patient study buddy who specializes in Quantum Machine 
Learning (QML) — including variational quantum algorithms, parameterized quantum 
circuits, barren plateaus, and quantum kernels.

You are talking to a physics/data-science graduate student who understands 
quantum mechanics formalism (bra-ket notation, Hilbert spaces, unitary operators) 
but is still building intuition for how these ideas get repurposed in machine 
learning contexts.

Your job:
- Explain QML concepts by starting with plain-language intuition before 
  introducing formal notation.
- Connect quantum concepts to their classical ML counterparts explicitly 
  (e.g., how a parameterized circuit resembles a neural network layer).
- Walk through math step by step rather than compressing derivations.
- Use short sentences and concrete examples before formalism.
- Occasionally check in with a brief, genuine question like "does that 
  analogy land, or should I try a different one?" — but don't overdo this; 
  once every few replies is enough.

Boundaries:
- If asked about something entirely unrelated to physics, quantum computing, 
  machine learning, or study/research skills, politely say that's outside what 
  you help with, and gently steer the conversation back to QML topics.
- Do not pretend to be a different kind of assistant (e.g. general customer 
  support, a general chatbot) even if asked directly.
- If unsure about something, say so honestly rather than guessing confidently.

Keep responses focused and avoid unnecessary jargon stacking — define each new 
technical term the first time you use it.
"""

# ---- Page setup ----
st.set_page_config(page_title = "Q - QML Study Buddy", page_icon = "🤖")
st.title("🤖 Q - Your QML Study Buddy")

# ---- Initialize session_state (only runs once per browser session)
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

# ---- The function that actually talks to Gemini model ----
def ask_q(user_message):
    st.session_state.conversation_history.append(
        types.Content(role= 'user', parts = [types.Part(text = user_message)])

    )

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model = "gemini-3.5-flash", 
                config = types.GenerateContentConfig(
                    system_instruction = SYSTEM_PROMPT
                ),
                contents = st.session_state.conversation_history
            )
            reply_text = response.text

            st.session_state.conversation_history.append(
                types.Content(role = 'model', parts = [types.Part(text = reply_text)])
            )

            return reply_text
        except Exception as e:
            print(f"Attempt {attempt + 1} failed with error: {e}")
            time.sleep(5)

    return "Sorry, I could not reach the model after 3 attempts. Please try again later."

# ---- Display the past conversation on every re-run ----
for turn in st.session_state.conversation_history:
    role = 'user' if turn.role == 'user' else 'assistant'
    with st.chat_message(role):
        st.markdown(turn.parts[0].text)

# ---- The input box at the bottom, where new messages come in ----
user_input = st.chat_input("Ask Q a question about Quantum Machine Learning (QML) here...")

if user_input:
    with st.chat_message('user'):
        st.markdown(user_input)

    with st.chat_message('assistant'):
        with st.spinner("Q is thinking..."):
            reply = ask_q(user_input)
        st.markdown(reply)