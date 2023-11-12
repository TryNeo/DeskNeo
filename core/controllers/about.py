import flet as ft


class About:
    def __init__(self, page: ft.Page):
        self.page = page

    def about(self, e: ft.ControlEvent) -> None:
        about = ft.AlertDialog(
                title=ft.Text("Acerca de la aplicacion - DeskNeo"),
                content=ft.Text("Aplicacion desarrollada por Joel Josue Huacon Lopez\nVersion:0.2.5\nLincencia:MIT\nGithub: https://github.com/TryNeo"),
            )
        self.page.dialog = about
        about.open = True
        self._update()

    def _update(self) -> None:
        self.page.update()