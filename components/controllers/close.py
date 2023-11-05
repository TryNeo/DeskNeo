import flet as ft

class Close:
    def __init__(self, page: ft.Page):
        self.page = page
        super().__init__()

    def close(self, e: ft.ControlEvent) -> None:
        self.page.window_close()