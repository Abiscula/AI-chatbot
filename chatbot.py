import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
IA_MODEL = "llama-3.3-70b-versatile"

client = Groq(
  api_key=GROQ_API_KEY,
)


def send_message(message, msg_list=[]):
  msg_list.append({ "role": "user", "content": message })

  chat_completion = client.chat.completions.create(
    messages = msg_list,
    model = IA_MODEL,
  )
  return chat_completion.choices[0].message

msg_list = []
while True:
  text = input("Escreva sua mensagem: ")

  if text.lower() == "sair":
    break
  else:
    response = send_message(text, msg_list)
    msg_list.append(response)
    print(response.content)