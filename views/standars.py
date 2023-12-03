import flet as ft
from flet_mvc import FletView
from utils.header import Header

class StandarsView(FletView):
    def __init__(self, controller, model,url):
        self.controller = controller
        self.model = model
        self.url = url
        self.view = ft.View(
            route=url,
            bgcolor = ft.colors.with_opacity(0.0, ft.colors.TRANSPARENT),
            floating_action_button=FloatingButton(page=controller.page,route_url="/").build(),
        )
        self.pages =[self._standars_page_one(),ft.Text("adsasdasd")]
        self.view.drawer = self._standars_drawer()
        self.view.appbar = self._standars_header()
        self.view.controls = self.pages
        self.controller.page.window_width = 1200
        self.controller.page.window_min_width = 810
        self.controller.page.window_height = 700
        super().__init__(model, self.view, controller)

    def _standars_header(self) -> object:
        title    = self.model.standars_title()
        info     = About(self.controller.page)
        #menu     = Menu(self.view)
        #close    = Close(self.controller.page)
        #minimized = Minimized(self.controller.page)
        #$return Header(
        #$    header_title=title,
        #$    visible_button_info=False,
        #$    menu=menu.menu,
        #$    about=info.about,
        #$    close=close.close,
        #$    minimized=minimized.minimized).build()
#$
    def _standars_drawer(self) -> ft.NavigationDrawer:
        navigation = ft.NavigationDrawer(
            data=self.pages,
            selected_index=0,
            on_change=self.controller.dest_change,
            bgcolor=ft.colors.with_opacity(3.3, ft.colors.TRANSPARENT),
            indicator_color="blue",
            shadow_color="gray",
            surface_tint_color="gray",
            elevation=3,
        )
        self.controller.standars_read_items_navs(navigation)
        self.controller.select_page(self.pages,navigation)
        return navigation
    

    def _standars_page_one(self) -> ft.Row:
        page_one_row = ft.Row(expand=True,spacing=5)
        page_one_markdonws = ft.Column(
            expand=True, scroll=ft.ScrollMode.HIDDEN,
        )

        page_one_row_right_panel = ft.Container(
            content=ft.Column(
                width=180,
                alignment=ft.MainAxisAlignment.START,
                controls=[
                        ft.Text("Tabla de contenido",weight=ft.FontWeight.W_400,size=18),
                ]
            )
        )

        for ik in self.model.standars_content("items-markdown-u"):
            if ik.get('id_content'):
                print(ik.get('id_content'))
                page_one_row_right_panel.content.controls.append(
                    ft.Container(
                        content=ft.Text(ik.get('title_markdown'),size=14),
                        on_click=lambda _: page_one_markdonws.scroll_to(key=ik.get('id'), duration=1000),
                    )
                )

        for mk in self.model.standars_content("items-markdown-u"):
            if mk.get('id_content'):
                page_one_markdonws.controls.append(Markdown(mk.get('title_markdown'),mk.get('content_markdown'),self.controller,mk.get('id')).main())
            if mk.get('comand_gif'):
                page_one_markdonws.controls.append(
                    Markdown(mk.get('title_markdown'),mk.get('content_markdown'),self.controller).comand_gif(mk.get('comand_gif_url'))
                )
        page_one_row.controls = [page_one_markdonws,page_one_row_right_panel]
        return page_one_row
    