import flet as ft
from typing import Type
from utils.header import Header
from utils.floatingbutton import FloatingButton
from flet_mvc import FletView,FletModel,FletController



class TextOpusView(FletView):
    def __init__(self, controller:Type[FletController], model:Type[FletModel],url:str):
        self.controller : Type[FletController] = controller
        self.model : Type[FletModel] = model
        self.url   : str = url
        self.view  : ft.View = self.__textopus_view()
        super().__init__(self.model, self.view, self.controller)

    def __textopus_view(self) -> ft.View:
        return ft.View(
            route=self.url,
            scroll=ft.ScrollMode.HIDDEN,
            controls=[
                ft.Container(
                    content=self.__textopus_body(),
                )
            ],
            appbar =self.__textopus_header(),
            bgcolor = ft.colors.with_opacity(0.0, ft.colors.TRANSPARENT),
            floating_action_button=FloatingButton(page=self.controller.page,route_url="/").build(),
        )
    

    def __textopus_header(self) -> ft.AppBar:
        return Header(page=self.controller.page,
            header_title=self.model.textopus_title()).build()
    
    def __textopus_body(self) -> ft.TextField:
        textfield : ft.TextField = ft.TextField(
            multiline=True,
            autocorrect=True,
            autofocus=True,
            border=ft.InputBorder.NONE,
            min_lines=100,
            content_padding=20,
            on_change=self.controller.save_textopus,
            cursor_color=ft.colors.GREEN,
            enable_suggestions=True,
        )
        textfield.value : str = self.controller.read_textopus()
        return textfield