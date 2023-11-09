from flet_mvc import FletView
from components.views.header import Header
from components.controllers.about import About
from components.controllers.change_theme import ChangeTheme
from components.controllers.close import Close
from components.controllers.minimized import Minimized
from components.views.floatingbutton import FloatingButton

import flet as ft

class WorkToolsView(FletView):
    def __init__(self, controller, model,url):
        self.controller = controller
        self.model = model
        self.url = url
        view = ft.View(
            route=url,
            controls=[
                self._worktools_header(),
                ft.Divider(),
            ],
            floating_action_button=FloatingButton(page=controller.page,route_url="/").build(),
        )
        super().__init__(model, view, controller)

    def _worktools_header(self) -> object:
        title    = "Herramientas de trabajo"
        theme    = ChangeTheme(self.controller.page)
        info     = About(self.controller.page)
        close    = Close(self.controller.page)
        minimized = Minimized(self.controller.page)
        return Header(
            header_title=title,
            visible_button_theme=False,
            about=info.about,
            close=close.close,
            minimized=minimized.minimized).build()