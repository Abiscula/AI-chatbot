import flet as ft

def build_input_field(on_send_click):
    input_field = ft.TextField(label="Digite sua mensagem...", expand=True)
    send_button = ft.ElevatedButton("Enviar", on_click=on_send_click)
    return input_field, send_button

def display_message(chat, message, is_user=True):
    prefix = "Você: " if is_user else "Bot: "
    chat.controls.append(ft.Text(f"{prefix}{message}"))
