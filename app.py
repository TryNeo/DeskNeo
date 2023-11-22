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

class DeskNeoApp:
    """
    The main application class for DeskNeo.
    """
    __TITLE = "DeskNeo - Ambiente personalizado"
    __PLATFORMS = ["android", "ios", "macos", "linux", "windows"]
    __WIDTH      = 550
    __HEIGHT     = 620
    __MAX_WIDTH  = 1200
    __MAX_HEIGHT = 850
    __MIN_WIDTH  = 550
    __MIN_HEIGHT = 340

    def __configure_app(self, page: ft.Page) -> None:
        """
        Configures the application settings.

        Args:
            page (ft.Page): The page object.

        Returns:
            None
        """
        def configure_title() -> None:
            """
            Configures the title of the page and hides the window title bar buttons and window title bar.
            """
            page.title = self.__TITLE
            page.window_title_bar_buttons_hidden = True
            page.window_title_bar_hidden = True

        def configure_window() -> None:
            """
            Configures the window properties.
            """
            page.window_center()
            page.window_width      = self.__WIDTH
            page.window_height     = self.__HEIGHT
            page.window_max_width  = self.__MAX_WIDTH
            page.window_max_height = self.__MAX_HEIGHT
            page.window_min_width  = self.__MIN_WIDTH
            page.window_min_height = self.__MIN_HEIGHT
        
        def configure_theme() -> None:
            """
            Configures the theme of the page.
            """
            theme = ft.Theme(use_material3=True, visual_density=ft.ThemeVisualDensity.COMFORTABLE)
            for platform in self.__PLATFORMS:
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
        configure_window()
        configure_theme()


    def __configure_routes(self, page: ft.Page) -> None:
        """
        Configures the routes for the application.

        Args:
            page (ft.Page): The page object.

        Returns:
            None
        """
        def path(url: str, clear: bool, view: ft.View, model: Type[FletModel], controller: Type[FletController]) -> list:
            """
            Creates a path configuration.

            Args:
                url (str): The URL path.
                clear (bool): Whether to clear the views.
                view (ft.View): The view class.
                model (Type[FletModel]): The model class.
                controller (Type[FletController]): The controller class.

            Returns:
                list: The path configuration.
            """
            return [url, clear, view, model, controller]

        def routes_add() -> list[list]:
            """
            Adds the routes for the application.

            Returns:
                list[list]: The list of route configurations.
            # Add your route configurations here
                routes_add()
                list[list]: The list of routes.
            """
            return [
                path(url="/", clear=True, view=HomeView, model=HomeModel, controller=HomeController),
                path(url="/work-tools", clear=True, view=WorkToolsView, model=WorkToolsModel, controller=WorkToolsController),
                path(url="/standars", clear=True, view=StandarsView, model=StandarsModel, controller=StandarsController),
                path(url="/text-opus", clear=True, view=TextOpusView, model=TextOpusModel, controller=TextOpusController),
            ]

        def page_add(url: str, view: ft.View, model=Type[FletModel], controller=Type[FletController]):
            """
            Adds a page to the views.

            Args:
                url (str): The URL path.
                view (ft.View): The view class.
                model (Type[FletModel]): The model class.
                controller (Type[FletController]): The controller class.

            Returns:
                None
            """
            model = model()
            controller = controller(page, model)
            model.controller = controller
            view = view(controller, model, url)
            return page.views.append(view.content)

        def routes(e: ft.ControlEvent):
            """
            Handles the route change event.

            Args:
                e (ft.ControlEvent): The control event.

            Returns:
                None
            """
            for url in routes_add():
                path_match = match(url[0], e.route)
                if path_match:
                    if url[1]:
                        page.views.clear()
                    page_add(url=url[0], view=url[2], model=url[3], controller=url[4])
                    break

        page.on_route_change = routes
        page.go(page.route)

    def __call__(self, flet_page: ft.Page):
        """
        Initializes the DeskNeoApp.

        Args:
            flet_page (ft.Page): The page object.

        Returns:
            None
        """
        self.page = flet_page
        self.__configure_app(self.page)
        self.__configure_routes(self.page)

if __name__ == "__main__":
    ft.app(target=DeskNeoApp(),assets_dir="assets")