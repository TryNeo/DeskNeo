import flet as ft
from typing import Final

class Header(ft.UserControl):
    def __init__(self, 
            page : ft.Page,
            header_title: str = "Ambiente - personal",
            **kwargs) -> None:
        super().__init__()
        self.page : ft.Page = page
        self.view : ft.View = kwargs.get('view', None)
        self.header_title : str = header_title
        self.button_enable_menu : bool = kwargs.get('button_enable_menu', True)

    def build(self) -> ft.AppBar:
        return ft.AppBar(
                leading=ft.WindowDragArea(
                    maximizable=False,
                    content=ft.Row(
                        [   
                            self.__button_menu(),
                            ft.Text(self.header_title, size=22, weight=ft.FontWeight.W_300)
                        ]
                    )
                ),
                automatically_imply_leading=True,
                leading_width=1200,
                bgcolor=ft.colors.with_opacity(0.0, ft.colors.TRANSPARENT),
                actions=[
                    self.__button_minimize(),
                    self.__button_close(),
                ],
            )

    def __button_menu(self) -> ft.IconButton:
        def menu(e:ft.ControlEvent) -> None:
            self.view.drawer.open = True
            self.view.update()

        return ft.IconButton(
                icon=ft.icons.MENU,
                style=ft.ButtonStyle(color=ft.colors.BLUE_500),
                selected=False,
                disabled=self.button_enable_menu,
                on_click=menu,
            )

    def __button_minimize(self) -> ft.IconButton:
        def minimized(e:ft.ControlEvent) -> None:
            self.page.window_minimized : bool = True
            self.page.update()
            
        return ft.IconButton(
                content=ft.Image(src="/icons/remove.svg", width=20, height=20, color=ft.colors.WHITE),
                on_click=minimized,
            )

    def __button_close(self) -> ft.IconButton:
        return ft.IconButton(
                icon=ft.icons.CLOSE,
                style=ft.ButtonStyle(color=ft.colors.RED_500),
                on_click=lambda _: self.page.window_close(),
            )
    

