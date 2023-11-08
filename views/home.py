import flet as ft
from typing import Type

from components.views.header import Header
from components.views.card import Card
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
            expand=1,
            child_aspect_ratio=3.5,
            width=1050,
            spacing=11,
            run_spacing=5,
            runs_count=2,
        )

        cards = self.model.home_cards_content("cards-content")
        for card in cards:
            if hasattr(self.controller,card.get('card_route')):
                try:
                    card_route = getattr(self.controller,card.get('card_route'))
                except Exception as e:
                    card_route = self.controller.error_method
            else:
                card_route = self.controller.error_method
            grid_card.controls.append(
                Card(
                    card_title=card.get('card_title'),
                    card_body=card.get('card_body'),
                    card_icon=card.get('card_icon'),
                    card_icon_color=card.get('card_icon_color'),
                    card_route=card_route,
                    card_disabled=card.get('card_disabled'),
                    controller=self.controller,
                ).build()
            )
        return grid_card