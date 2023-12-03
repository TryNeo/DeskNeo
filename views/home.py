import flet as ft
from typing import Type,Final
from utils.header import Header
from flet_mvc import FletView,FletModel,FletController

class HomeView(FletView):
    def __init__(self, controller:Type[FletController], model:Type[FletModel],url:str):
        self.controller : Type[FletController] = controller
        self.model : Type[FletModel] = model
        self.url   : str = url
        self.view  : ft.View = self.__home_view()
        self.__home_configure()
        super().__init__(self.model, self.view, self.controller)

    def __home_view(self) -> ft.View:
        return ft.View(
            route=self.url,
            controls=[
                ft.Card(
                    elevation=2,
                    color=ft.colors.with_opacity(0.0, ft.colors.TRANSPARENT),
                    scale= ft.transform.Scale(scale=0.98),
                    col={"sm": 12, "md": 6, "xl": 6},
                    content=ft.Container(
                        border_radius=10,
                        ink=True,
                        bgcolor=ft.colors.with_opacity(0.0, ft.colors.TRANSPARENT),
                        content=ft.Column(
                            [
                                ft.ListTile(
                                    width=1200,
                                    title=ft.Text(
                                        value=f"Hola , {self.controller.get_name_user()}",
                                        size=18,weight=ft.FontWeight.W_300
                                    ),
                                    trailing=ft.Row(
                                        [
                                            ft.Text("[BETA]",size=12,weight=ft.FontWeight.W_700,color="green"),
                                            self.__home_about(),
                                        ],
                                        width=75,
                                    )
                                )
                            ]
                        ),
                    )
                ),
                self.__home_body(),
            ],
            appbar=self.__home_header(),
            bgcolor = ft.colors.with_opacity(0.0, ft.colors.TRANSPARENT),
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.MainAxisAlignment.CENTER,
        )

    def __home_configure(self) -> None:
        self.controller.page.window_height    : int = 640
        self.controller.page.window_width     : int = 490
        self.controller.page.window_min_width : int = 490

    def __home_header(self) -> ft.AppBar:
        return Header(page=self.controller.page).build()
    
    def __home_about(self) -> ft.IconButton:
        def about(e : ft.ControlEvent) -> None:
            license : Final[str] = "https://raw.githubusercontent.com/TryNeo/DeskNeo/master/LICENSE"
            github  : Final[str] = "https://github.com/TryNeo/"
            value   : Final[str] = """Aplicacion desarrollada por Josue Lopez \n
Version : 1.3.0 \n
Github  : [{GITHUB}]({GITHUB}) \n
Licensia: [MIT]({LICENSE}) \n
"""
            info : ft.AlertDialog = ft.AlertDialog(
                    title=ft.Text("Acerca de la aplicacion"),
                    content=ft.Markdown(
                        value=value.format(GITHUB=github, LICENSE=license),
                        selectable=True,
                        extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
                        on_tap_link=lambda e: self.controller.page.launch_url(e.data),
                    )
                )
            self.controller.page.dialog : ft.AlertDialog = info
            info.open :bool = True
            self.controller.page.update()

        return ft.IconButton(
                icon=ft.icons.INFO_OUTLINED,
                style=ft.ButtonStyle(color=ft.colors.INDIGO_500),
                on_click=about,
                tooltip="Acerca de",
            )

    def __home_body(self) -> ft.Column:
        responsive_cards : ft.ResponsiveRow = ft.ResponsiveRow()
        self.controller.responsive_cards(responsive_cards)
        return ft.Column(controls=[responsive_cards],scroll=ft.ScrollMode.HIDDEN,expand=True)