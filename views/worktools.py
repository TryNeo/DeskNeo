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
        self.view = ft.View(
            route=url,
            scroll=ft.ScrollMode.HIDDEN,
            controls=[
                self._worktools_body(),
            ],
            appbar=self._worktools_header(),
            bgcolor = ft.colors.with_opacity(0.0, ft.colors.TRANSPARENT),
            floating_action_button=FloatingButton(page=controller.page,route_url="/").build(),
        )
        super().__init__(model, self.view, controller)

    def _worktools_header(self) -> object:
        title    = self.model.worktools_title()
        info     = About(self.controller.page)
        close    = Close(self.controller.page)
        minimized = Minimized(self.controller.page)
        return Header(
            header_title=title,
            visible_button_menu=False,
            about=info.about,
            close=close.close,
            minimized=minimized.minimized).build()
    
    def _worktools_body(self) -> ft.Column:
        worktool_responsive_row = ft.ResponsiveRow(spacing=12)
        self.controller.worktools_read_cards(worktool_responsive_row)
        return ft.Column(
            height=1200,width=1200,
            run_spacing=50,
            controls=[
                worktool_responsive_row,
            ]
        )
