import flet as ft


class Menu:
    def __init__(self, view: ft.View):
        self.view = view

    def menu(self, e: ft.ControlEvent) -> None:
        self.view.drawer.open = True
        self.view.update()