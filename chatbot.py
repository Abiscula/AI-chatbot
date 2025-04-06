import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
IA_MODEL = "llama-3.3-70b-versatile"

client = Groq(
  api_key=GROQ_API_KEY,
)


def send_message(message):
  chat_completion = client.chat.completions.create(
    messages=[
      {
        "role": "user",
        "content": message,
      }
    ],
    model=IA_MODEL,
  )
  return chat_completion.choices[0].message.content


# Teste
print(send_message("Em que ano einstein publicou a teoria geral da relatividade?"))
