from flet_mvc import FletView
from core.views.header import Header
from core.controllers.about import About
from core.controllers.close import Close
from core.controllers.minimized import Minimized
from core.views.floatingbutton import FloatingButton

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
        title    = self.model.worktools_title()
        info     = About(self.controller.page)
        close    = Close(self.controller.page)
        minimized = Minimized(self.controller.page)
        return Header(
            header_title=title,
            visible_button_theme=False,
            about=info.about,
            close=close.close,
            minimized=minimized.minimized).build()