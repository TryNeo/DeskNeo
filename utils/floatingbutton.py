import flet as ft

class FloatingButton:
    def __init__(self, page:ft.Page,route_url:str):
        self._route_url = route_url
        self.page = page

    def build(self) -> ft.FloatingActionButton:
        return ft.FloatingActionButton(
            icon=ft.icons.SUBDIRECTORY_ARROW_LEFT,
            on_click=lambda _: self.page.go(self._route_url),
            bgcolor = ft.colors.SURFACE,
            mini=True,
        )