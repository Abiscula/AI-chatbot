from src.chatbot.core import send_message
from src.ui.components import build_input_field, display_message
import flet as ft

def app_controller(page: ft.Page):
  page.title = "Chatbot com Groq"
  page.theme_mode = ft.ThemeMode.DARK

  messages = []

  chat_column = ft.Column(
    spacing=10,
    scroll=ft.ScrollMode.AUTO
  )

  def on_send_click(e):
    user_input = input_field.value.strip()
    if user_input == "":
      return

    display_message(chat_column, user_input, is_user=True)
    response = send_message(user_input, messages)
    messages.append(response)
    display_message(chat_column, response.content, is_user=False)

    input_field.value = ""
    page.update()

  input_field, send_button = build_input_field(on_send_click)

  # Layout principal com chat expandindo e input fixo no rodapé
  layout = ft.Column(
    controls=[
      ft.Container(
        content=chat_column,
        expand=True,
        padding=ft.Padding(10, 20, 10, 10)
      ),
      ft.Divider(),
      ft.Container(
        ft.Row(
          [input_field, send_button],
          alignment=ft.MainAxisAlignment.CENTER,
        ),
        padding=10,
      )
    ],
    expand=True
  )

  page.add(layout)
