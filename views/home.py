import flet as ft
from typing import Type

from components.views.header import Header
from components.views.card import Card
from components.controllers.about import About
from components.controllers.change_theme import ChangeTheme
from components.controllers.close import Close
from components.controllers.minimized import Minimized

from flet_mvc import FletView, FletModel, FletController


class HomeView(FletView):
    def __init__(self, controller, model,url):
        self.url = url
        view = ft.View(
            route=url,
            controls=[
                self._home_header(controller, model),
                ft.Divider(),
                self._home_body(controller, model),
            ],
        )
        self._home_body(controller, model)
        super().__init__(model, view, controller)


    def _home_header(self,controller:Type[FletController],model: Type[FletModel]) -> object:
        username = controller.get_name_user()
        title    = model.home_title(value=username)
        theme    = ChangeTheme(controller.page)
        info     = About(controller.page)
        close    = Close(controller.page)
        minimized = Minimized(controller.page)
        return Header(
            header_title=title,
            change_theme=theme.change_theme,
            about=info.about,
            close=close.close,
            minimized=minimized.minimized).header()
    
    def _home_body(self,controller:Type[FletController],model: Type[FletModel]):
        grid_card = ft.GridView(
            max_extent=640,
            child_aspect_ratio=3.3,
        )

        cards = model.home_cards()
        for card in cards:
            grid_card.controls.append(
                Card(
                    card_title=card.get('card_title'),
                    card_body=card.get('card_body'),
                    card_icon=card.get('card_icon'),
                    card_color=card.get('card_color'),
                    card_route=card.get('card_route'),
                    card_disabled=card.get('card_disabled')
                ).build()
            )
        return grid_card