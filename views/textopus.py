from flet_mvc import FletView
from core.views.header import Header
from core.controllers.about import About
from core.controllers.close import Close
from core.controllers.minimized import Minimized
from core.views.floatingbutton import FloatingButton

import flet as ft

class TextOpusView(FletView):
    def __init__(self, controller, model,url):
        self.controller = controller
        self.model = model
        self.url = url
        view = ft.View(
            route=url,
            scroll=ft.ScrollMode.HIDDEN,
            controls=[
                self._textopus_header(),
                self._textopus_body(),
            ],
            floating_action_button=FloatingButton(page=controller.page,route_url="/").build(),
        )
        super().__init__(model, view, controller)

    def _textopus_header(self) -> object:
        title    = self.model.textopus_title()
        info     = About(self.controller.page)
        close    = Close(self.controller.page)
        minimized = Minimized(self.controller.page)
        return Header(
            header_title=title,
            visible_button_theme=False,
            about=info.about,
            close=close.close,
            minimized=minimized.minimized).build()
    
    def _textopus_body(self) -> ft.TextField:
        textfield = ft.TextField(
            multiline=True,
            autocorrect=True,
            autofocus=True,
            border=ft.InputBorder.NONE,
            min_lines=100,
            content_padding=20,
            on_change=self.controller.save_textopus,
            cursor_color=ft.colors.GREEN,
        )
        textfield.value = self.controller.read_textopus()
        return textfield