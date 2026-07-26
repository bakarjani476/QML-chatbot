import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get('GOOGLE_API_KEY')
client = genai.Client(api_key = api_key)

# give the system prompt to the model
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
technical term the first time you use it."""

# To store the history of the conversation, we can use a list to keep track of user messages and model responses. This will allow the model to have context for the conversation.
conversation_history = []

def ask_q(user_message):
    # Add the user's new message to the running history of the conversation
    conversation_history.append(
        types.Content(role= 'user', parts=[types.Part(text = user_message)])  # this is the SDK's structured way of representing one turn of conversation
    )
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model = "gemini-3.5-flash",
                config = types.GenerateContentConfig(
                    system_instruction = SYSTEM_PROMPT

                ),
                contents = conversation_history  # send the whole history ot just this message
            )
            reply_text = response.text

            # Add the model's response to the conversation history too, so future messages have context
            conversation_history.append(
                types.Content(role = 'model', parts = [types.Part(text = reply_text)])
            )

            return reply_text
        
        except Exception as e:
            print(f"Attempt {attempt + 1} failed with error: {e}")
            time.sleep(5)

    return "Sorry, I could not reach the model after 3 attempts. Please try again later."

print("Q is ready to chat! Type your question about Quantum Machine Learning (QML) below. Type 'quit' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print('Q: Good luck with your research! See you next time.')
        break

    reply = ask_q(user_input)
    print(f"Q: {reply}\n")