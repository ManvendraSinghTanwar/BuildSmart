import os
from dotenv import load_dotenv
from openai import OpenAI

# Load OpenAI API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def get_chatbot_response(user_input):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_input}],
    )
    return response.choices[0].message.content
