import os
import time
from dotenv import load_dotenv
from google import genai

# load the .env file into memory so os.environ can see or access it
loaded = load_dotenv()
print("Did .env load?", loaded)

# Read the API key from the environment
api_key = os.environ.get('GOOGLE_API_KEY')
print("API key found:", api_key)

# Create a GenAI client -- this object handles all the communication with Gemini's servers
client = genai.Client(api_key=api_key)

# Send one message to the Gemini API and get a response back
for attempt in range(3):
    try:
        response = client.models.generate_content(
            model = "gemini-3.5-flash",
            contents = "Say hello and tell me a fun fact about quantum computers."
        )
        print(response.text)
        break  # Exit the loop if the request was successful
    except Exception as e:
        print(f"Attempt {attempt + 1} failed: {e}")
        time.sleep(5)  # Wait before retrying
    

