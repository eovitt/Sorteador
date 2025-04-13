import flet as ft
import random

def main(page: ft.Page):
    page.title = "Sorteador de Nomes"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

# Função chamada quando o botão de sortear é clicado
    def sortear_clicked(e):
        names = [name.strip() for name in name_input.value.split(",") if name.strip()]
        if names:
            sorteado = random.choice(names)
            result_text.value = f"Nome sorteado: {sorteado}"
        else:
            result_text.value = "Por favor, insira pelo menos um nome."
        page.update()

# Função chamada quando o botão de limpar é clicado
    def limpar_clicked(e):
        name_input.value = ""
        result_text.value = ""
        page.update()

# Criação dos elementos da interface
    title = ft.Text("Sorteador de Nomes", style="headlineMedium")
    name_input = ft.TextField(label="Digite os nomes separados por vírgula:", width=400)
    sortear_button = ft.ElevatedButton(text="Sortear", on_click=sortear_clicked)
    limpar_button = ft.ElevatedButton(text="Limpar", on_click=limpar_clicked)
    result_text = ft.Text()

# Organizando os elementos em um contêiner
    content = ft.Column(
        controls=[
            title,
            name_input,
            ft.Row([sortear_button, limpar_button], alignment=ft.MainAxisAlignment.CENTER),
            result_text
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20
    )

# Adicionando o contêiner à 
    page.add(content)

# Executando a aplicação
ft.app(target=main)