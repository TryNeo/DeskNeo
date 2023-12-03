import flet as ft
from typing import Type
from flet_mvc import FletView,FletModel,FletController
from utils.header import Header
from utils.floatingbutton import FloatingButton
class WorkToolsView(FletView):
    def __init__(self, controller:Type[FletController], model:Type[FletModel],url:str):
        self.controller : Type[FletController] = controller
        self.model : Type[FletModel] = model
        self.url   : str = url
        self.view  : ft.View = self.__worktools_view()
        super().__init__(self.model, self.view, self.controller)

    def __worktools_view(self) -> ft.View:
        return ft.View(
            route=self.url,
            controls=[
                self.__worktools_body(),
            ],
            appbar=self.__worktools_header(),
            bgcolor = ft.colors.with_opacity(0.0, ft.colors.TRANSPARENT),
            floating_action_button=FloatingButton(page=self.controller.page,route_url="/").build(),
        )
    
    def __worktools_header(self) -> ft.AppBar:
        return Header(page=self.controller.page,
            header_title=self.model.worktools_title()).build()
    
    def __worktools_body(self) -> ft.Column:
        worktool_responsive_row : ft.ResponsiveRow = ft.ResponsiveRow(spacing=12)
        self.controller.worktools_read_cards(worktool_responsive_row)
        return ft.Column(
            height=1200,width=1200,
            run_spacing=50,
            scroll=ft.ScrollMode.HIDDEN,expand=True,
            controls=[
                worktool_responsive_row,
            ]
        )
