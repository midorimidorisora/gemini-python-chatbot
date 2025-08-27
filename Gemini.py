import google.generativeai as genai
from api import Gemini_API_KEY as api
import os

genai.configure(api_key=os.getenv("Gemini_API_KEY"))
model = genai.GenerativeModel('gemini-2.5-flash')
chat = model.start_chat(history=[])
while True:
    user_input = input("\nYou: ")

    response = chat.send_message(user_input)
    print("AI:", response.text)
