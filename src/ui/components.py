import flet as ft

def build_input_field(on_send_click):
    input_field = ft.TextField(
        label="Digite sua mensagem...", 
        expand=True, 
        autofocus=True,
      )
    send_button = ft.ElevatedButton("Enviar", on_click=on_send_click)
    return input_field, send_button

def display_message(chat_column, message, is_user=True):
  chat_column.controls.append(
    ft.Container(
      content=ft.Text(
        f"{'Você' if is_user else 'Bot'}: {message}",
      ),
      padding=ft.Padding(5, 20, 5, 5),
      alignment=ft.alignment.center_left
    )
  )

  if not is_user:
    chat_column.controls.append(
    ft.Divider(thickness=1, color=ft.colors.with_opacity(0.2, ft.colors.WHITE))
  )