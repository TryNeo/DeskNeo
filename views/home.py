import flet as ft
from typing import Type

from core.views.header import Header
from core.controllers.about import About
from core.controllers.close import Close
from core.controllers.minimized import Minimized

from flet_mvc import FletView


class HomeView(FletView):
    def __init__(self, controller, model,url):
        self.controller = controller
        self.model = model
        self.url = url
        self.view = ft.View(
            route=url,
            scroll=ft.ScrollMode.HIDDEN,
            controls=[
                self._home_body(),
            ],
            appbar=self._home_header(),
            bgcolor = ft.colors.with_opacity(0.0, ft.colors.TRANSPARENT),
        )
        super().__init__(model, self.view, controller)


    def _home_header(self) -> object:
        username  = self.controller.get_name_user()
        title     = self.model.home_title(value=username)
        info      = About(self.controller.page)
        close     = Close(self.controller.page)
        minimized = Minimized(self.controller.page)
        return Header(
            header_title=title,
            visible_button_menu=False,
            about=info.about,
            close=close.close,
            minimized=minimized.minimized).build()
    
    def _home_body(self) -> ft.Column:
        responsive_cards = ft.ResponsiveRow()
        self.controller.responsive_cards(responsive_cards,self.controller)
        return ft.Column(height=800,width=1200,controls=[
            responsive_cards,
        ])