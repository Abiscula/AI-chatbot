from src.chatbot.core import send_message
from src.ui.components import build_input_field, display_message
import flet as ft

def app_controller(page: ft.Page):
    page.title = "Chatbot com Groq"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = "auto"

    chat = ft.Column()
    messages = []

    def on_send_click(e):
        user_input = input_field.value.strip()
        if user_input == "":
            return
        display_message(chat, user_input, is_user=True)

        response = send_message(user_input, messages)
        messages.append(response)
        display_message(chat, response.content, is_user=False)

        input_field.value = ""
        page.update()

    input_field, send_button = build_input_field(on_send_click)

    page.add(chat, ft.Row([input_field, send_button]))
