from flet_mvc import FletView
from core.views.header import Header
from core.controllers.menu import Menu
from core.controllers.about import About
from core.controllers.close import Close
from core.controllers.minimized import Minimized
from core.views.floatingbutton import FloatingButton

import flet as ft

class StandarsView(FletView):
    def __init__(self, controller, model,url):
        self.controller = controller
        self.model = model
        self.url = url
        self.pages =[
            ft.Column(
                [
                    ft.Text("Item 1", size=22, weight=ft.FontWeight.W_100),
                ]
            ),
            ft.Column(
                [
                    ft.Text("Item 2", size=22, weight=ft.FontWeight.W_100),
                ]
            ),
        ]

        self.view = ft.View(
            route=url,
            scroll=ft.ScrollMode.HIDDEN,
            controls=[
                ft.Column(
                    self.pages,
                    scroll="auto",
                    expand=True,
                ),
            ],
            drawer=self._standars_drawer(),
            bgcolor = ft.colors.with_opacity(0.0, ft.colors.TRANSPARENT),
            floating_action_button=FloatingButton(page=controller.page,route_url="/").build(),
        )
        self.view.appbar = self._standars_header()
        self.controller.page.window_width = 900
        self.controller.page.window_height = 700
        super().__init__(model, self.view, controller)

    def _standars_header(self) -> object:
        title    = self.model.standars_title()
        info     = About(self.controller.page)
        menu     = Menu(self.view)
        close    = Close(self.controller.page)
        minimized = Minimized(self.controller.page)
        return Header(
            header_title=title,
            visible_button_info=False,
            menu=menu.menu,
            about=info.about,
            close=close.close,
            minimized=minimized.minimized).build()


    def _standars_drawer(self) -> ft.NavigationDrawer:
        navigation = ft.NavigationDrawer(
            data=self.pages,
            selected_index=0,
            on_change=self.controller.dest_change,
            bgcolor=ft.colors.with_opacity(1.3, ft.colors.TRANSPARENT),
            indicator_color="blue",
            elevation=3,
        )
        self.controller.standars_read_items_navs(navigation)
        self.controller.select_page(self.pages,navigation)
        return navigation