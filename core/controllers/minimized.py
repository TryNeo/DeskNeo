import flet as ft


class Minimized:
    def __init__(self, page: ft.Page):
        self.page = page

    def minimized(self, e: ft.ControlEvent) -> None:
        self.page.window_minimized = True
        self._update()

    def _update(self) -> None:
        self.page.update()