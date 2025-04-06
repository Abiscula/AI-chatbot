import flet as ft
from src.chatbot import send_message

def main(page: ft.Page):
  page.title = "Chatbot com Groq"
  page.theme_mode = ft.ThemeMode.DARK
  page.scroll = "auto"

  messages = []
  chat = ft.Column()

  input_field = ft.TextField(label="Digite sua mensagem...", expand=True)

  def send_click(e):
    user_msg = input_field.value.strip()
    if user_msg == "":
        return

    user_message(user_msg)
    response = get_AI_message(user_msg)
    show_AI_response(response)

  send_button = ft.ElevatedButton("Enviar", on_click=send_click)

  def user_message(user_msg):
    chat.controls.append(ft.Text(f"Você: {user_msg}"))
    page.update()

  def get_AI_message(user_msg):
    response = send_message(user_msg, messages)
    messages.append(response)
    return response;

  def show_AI_response(response):
    chat.controls.append(ft.Text(f"Bot: {response.content}"))
    input_field.value = ""
    page.update()

  page.add(
      chat,
      ft.Row([input_field, send_button])
  )

ft.app(target=main)
