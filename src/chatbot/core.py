import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
IA_MODEL = "llama3-70b-8192"

client = Groq(api_key=GROQ_API_KEY)

def send_message(message, msg_list=[]):
    msg_list.append({"role": "user", "content": message})

    chat_completion = client.chat.completions.create(
        messages=msg_list,
        model=IA_MODEL,
    )
    return chat_completion.choices[0].message
