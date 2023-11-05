import flet as ft

class Header:
    def __init__(self, header_title: str='Default title', visible_button_theme: bool=True, **kwargs):
        self._header_title = header_title
        self._visible_button = visible_button_theme
        self._change_theme = kwargs.get('change_theme', None)
        self._about = kwargs.get('about', None)
        self._close = kwargs.get('close', None)
        self._minimized = kwargs.get('minimized', None)
        
        super().__init__()

    def header(self) -> ft.Container:
        return ft.Container(
                content=ft.Row(
                    controls=[
                        self._window_drag_area_head(),
                        self._icon_button_change_theme(),
                        self._icon_button_about(),
                        self._icon_button_minimize(),
                        self._icon_button_close(),
                    ]
                ),
            )
    
    def _window_drag_area_head(self) -> ft.WindowDragArea:
        return ft.WindowDragArea(
                ft.Container(
                    ft.Text(self._header_title, size=26, weight=ft.FontWeight.W_100),
                    padding=9,
                ),
                expand=True,
            )

    def _icon_button_change_theme(self) -> ft.IconButton:
        return ft.IconButton(
                icon=ft.icons.NIGHTLIGHT_ROUND,
                selected_icon=ft.icons.SUNNY,
                on_click=self._change_theme,
                selected=False,
                style=ft.ButtonStyle(color={"selected": ft.colors.ORANGE_500, "": ft.colors.YELLOW_700}),
                visible=self._visible_button,
                tooltip="Cambiar tema",
            )
    
    def _icon_button_about(self) -> ft.IconButton:
        return ft.IconButton(
                icon=ft.icons.INFO,
                style=ft.ButtonStyle(color=ft.colors.BLUE_500),
                tooltip="Acerca de",
                on_click=self._about,
            )
    
    def _icon_button_close(self) -> ft.IconButton:
        return ft.IconButton(
                icon=ft.icons.CLOSE,
                style=ft.ButtonStyle(color=ft.colors.RED_500),
                tooltip="Cerrar",
                on_click=self._close,
            )
    
    def _icon_button_minimize(self) -> ft.IconButton:
        return ft.IconButton(
                content=ft.Image(src="/icons/bag-remove.svg", width=20, height=20, color=ft.colors.BLUE_ACCENT_200),
                tooltip="Minimizar",
                on_click=self._minimized,
            )
