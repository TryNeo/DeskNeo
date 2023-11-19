import flet as ft
from flet_mvc import FletModel,FletController

# Models
from models.home import HomeModel
from models.worktools import WorkToolsModel
from models.textopus import TextOpusModel
from models.standars import StandarsModel

# Views
from views.home import HomeView
from views.worktools import WorkToolsView
from views.textopus import TextOpusView
from views.standars import StandarsView

# Controllers
from controllers.home import HomeController
from controllers.worktools import WorkToolsController
from controllers.textopus import TextOpusController
from controllers.standars import StandarsController

from typing import Type
from repath import match


def path(url: str, clear: bool, view: ft.View, model:Type[FletModel], controller:Type[FletController]) -> list:
    return [url,clear, view, model, controller]

class DeskNeoApp:
    def __init__(self):
        self.app_routes: list[list] = [
            path(url="/", clear=True,view=HomeView, model=HomeModel, controller=HomeController),
            path(url="/work-tools", clear=True,view=WorkToolsView, model=WorkToolsModel, controller=WorkToolsController),
            path(url="/standars", clear=True,view=StandarsView, model=StandarsModel, controller=StandarsController),
            path(url="/text-opus", clear=True,view=TextOpusView, model=TextOpusModel, controller=TextOpusController),
        ]

    def _configure_app(self,page: ft.Page) -> None:
        def configure_title():
            page.title = "DeskNeo - Ambiente personalizado"
            page.window_title_bar_buttons_hidden = True
            page.window_title_bar_hidden = True

        def configure_size() -> None:
            page.window_center()
            page.window_width = 550
            page.window_height = 620
            page.window_max_width = 1200
            page.window_max_height = 850
            page.window_min_width = 550
            page.window_min_height =340
        
        def configure_theme() -> None:
            theme = ft.Theme(use_material3=True,visual_density=ft.ThemeVisualDensity.COMFORTABLE)
            platforms = ["android", "ios", "macos", "linux", "windows"]
            for platform in platforms:
                setattr(theme.page_transitions, platform, ft.PageTransitionTheme.NONE)
            theme.scrollbar_theme = ft.ScrollbarTheme(
                    track_color={
                        ft.MaterialState.DEFAULT: ft.colors.TRANSPARENT,
                    },
                    track_visibility=True,
                    thickness=2,
                    radius=15,
                    main_axis_margin=5,
                )
            page.theme = theme
            page.theme_mode = ft.ThemeMode.DARK
            page.update()

        configure_title()
        configure_size()
        configure_theme()


    def _configure_routes(self,page: ft.Page) -> None:
        def page_add(url: str, view: ft.View, model=Type[FletModel], controller=Type[FletController]):
            model = model()
            controller = controller(page, model)
            model.controller = controller
            view = view(controller, model, url)
            return page.views.append(view.content)

        def routes(e:ft.ControlEvent):
            for url in self.app_routes:
                path_match = match(url[0], e.route)
                if path_match:
                    if url[1]:
                        page.views.clear()
                    page_add(url=url[0], view=url[2], model=url[3], controller=url[4])
                    break
        page.on_route_change = routes
        page.go(page.route)

    def __call__(self, flet_page: ft.Page):
        self.page = flet_page
        self._configure_app(self.page)
        self._configure_routes(self.page)


if __name__ == "__main__":
    ft.app(target=DeskNeoApp(),assets_dir="assets")