import flet as ft

def main(page: ft.Page):

    page.bgcolor = "#0474DB"
    page.window.width = 450
    page.window.height = 800
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER

    # Função para configurar a página inicial
    def home_page():
        page.controls.clear()
        page.add(
            ft.Container(
                padding=ft.padding.only(top=20),
                content=ft.Text(
                    "Bem vindo(a) de volta!",
                    size=50,
                    color="#e6e6e6",
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                ),
            )
        )

        login = ft.TextField(
            hint_text="Email:",
            bgcolor=ft.colors.WHITE,
            prefix_icon=ft.icons.PERSON,
            text_style=ft.TextStyle(color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
            border_radius=24,
        )

        senha = ft.TextField(
            hint_text="Senha:",
            prefix_icon=ft.icons.LOCK,
            password=True,
            can_reveal_password=True,
            bgcolor=ft.colors.WHITE,
            text_style=ft.TextStyle(color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
            border_radius=24,
        )

        page.add(
            ft.Container(
                margin=ft.margin.only(top=30),
                bgcolor=ft.colors.WHITE70,
                width=430,
                height=430,
                border_radius=8,
                padding=ft.padding.only(top=65, left=15, right=15),
                content=ft.Column(
                    [
                        login,
                        senha,
                        ft.ElevatedButton(
                            text="Entrar",
                            color=ft.colors.WHITE,
                            bgcolor=ft.colors.ORANGE_700,
                            width=400,
                            height=40,
                        ),
                        ft.Row(
                            controls=[
                                ft.Container(
                                    ft.TextButton(
                                        content=ft.Text(
                                            "Recuperar senha",
                                            color=ft.Colors.ORANGE,
                                        )
                                    ),
                                    border=ft.border.all(2, ft.Colors.ORANGE),
                                    border_radius=24,
                                    bgcolor=ft.colors.WHITE
                                ),
                                ft.Container(
                                    ft.ElevatedButton(
                                        content=ft.Text(
                                            "Sou novo por aqui",
                                            color=ft.colors.ORANGE,
                                        ),
                                        bgcolor=ft.colors.WHITE,
                                        on_click=lambda _: page.go("/register"),
                                    ),
                                    border=ft.border.all(2, ft.Colors.ORANGE),
                                    border_radius=24,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                    ],
                    spacing=30,
                ),
            )
        )
        page.update()

    # REgistro
    def register_page():
        page.controls.clear()
        page.add(
            ft.Text(
                "Crie sua conta!",
                size=45,
                color="#e6e6e6",
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER
            ),

            ft.Container(
                margin=ft.margin.only(top=80),
                bgcolor=ft.colors.WHITE70,
                width=430,
                height=630,
                border_radius=8,
                padding=ft.padding.only(top=60, left=15, right=15),

                content=ft.Column([
                    ft.TextField(
                                    hint_text="Nome:",
                                    bgcolor=ft.colors.WHITE,
                                    text_style=ft.TextStyle(color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
                                    border_radius=24
                                ),

                    ft.TextField(
                                    hint_text="Sobrenome:",
                                    bgcolor=ft.colors.WHITE,
                                    text_style=ft.TextStyle(color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
                                    border_radius=24
                                ),
                    ft.TextField(
                                    hint_text="Email:",
                                    bgcolor=ft.colors.WHITE,
                                    prefix_icon=ft.icons.PERSON,
                                    text_style=ft.TextStyle(color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
                                    border_radius=24
                                ),
                    ft.TextField(
                                    hint_text="Crie uma senha:",
                                    prefix_icon=ft.icons.LOCK,
                                    password=True,
                                    can_reveal_password=True,
                                    bgcolor=ft.colors.WHITE,
                                    text_style=ft.TextStyle(color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
                                    border_radius=24
                                ),
                    ft.TextField(
                                    hint_text="Confirme a senha:",
                                    prefix_icon=ft.icons.LOCK,
                                    password=True,
                                    can_reveal_password=True,
                                    bgcolor=ft.colors.WHITE,
                                    text_style=ft.TextStyle(color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
                                    border_radius=24
                                ),
                    ft.ElevatedButton(
                                        text='Criar conta',
                                        color=ft.colors.WHITE,
                                        bgcolor=ft.colors.ORANGE_700,
                                        width=400,
                                        height=40
                                    ),            
                    ft.TextButton(
                                        content=ft.Text(
                                            "Já tenho uma conta",
                                            color=ft.Colors.BLACK,
                                            style = ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE)
                                        ),
                                        on_click=lambda _: page.go("/")
                                     )
                ],
                spacing=30
                )
            ),
            
        )
        page.update()

    def route_change(e):
        if page.route == "/":
            home_page()
        elif page.route == "/register":
            register_page()

    page.on_route_change = route_change
    page.go("/") 

ft.app(target=main)
