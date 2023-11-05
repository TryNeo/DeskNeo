import flet as ft

class ChangeTheme:
    def __init__(self, page: ft.Page):
        self.page = page
        super().__init__()

    def change_theme(self, e: ft.ControlEvent) -> None:
        if self.page.theme_mode == ft.ThemeMode.DARK:
            e.control.selected = not e.control.selected
            self.page.theme_mode = ft.ThemeMode.LIGHT
        else:
            e.control.selected = not e.control.selected
            self.page.theme_mode = ft.ThemeMode.DARK
        self._update()

    def _update(self) -> None:
        self.page.update()