import flet as ft
from typing import Type

from components.views.header import Header
from components.controllers.about import About
from components.controllers.change_theme import ChangeTheme
from components.controllers.close import Close
from components.controllers.minimized import Minimized
from flet_mvc import FletView


class HomeView(FletView):
    def __init__(self, controller, model,url):
        self.controller = controller
        self.model = model
        self.url = url
        view = ft.View(
            route=url,
            controls=[
                self._home_header(),
                ft.Divider(),
                self._home_body(),
            ],
        )
        super().__init__(model, view, controller)


    def _home_header(self) -> object:
        username = self.controller.get_name_user()
        title    = self.model.home_title(value=username)
        theme    = ChangeTheme(self.controller.page)
        info     = About(self.controller.page)
        close    = Close(self.controller.page)
        minimized = Minimized(self.controller.page)
        return Header(
            header_title=title,
            change_theme=theme.change_theme,
            about=info.about,
            close=close.close,
            minimized=minimized.minimized).build()
    
    def _home_body(self) -> ft.GridView:
        grid_card = ft.GridView(
            child_aspect_ratio=3.5,
            width=1050,
            spacing=11,
            run_spacing=5,
            runs_count=2,
        )
        self.controller.grid_cards(grid_card,self.controller)
        return grid_card