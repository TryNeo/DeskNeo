import flet as ft
class Card(ft.UserControl):
    def __init__(self,
                page : ft.Page,
                title:str,
                description:str,
                icon:str,
                icon_color:str,
                route:str,
                disabled:bool):
        super().__init__()
        self.page        : ft.Page = page
        self.title       : str  = title
        self.description : str  = description
        self.icon        : str  = icon
        self.icon_color  : str  = icon_color
        self.route       : str  = route
        self.disabled    : bool = disabled
        self.card        : ft.Card = None

    def build(self,method_redirect) -> ft.Card:
        self.card = ft.Card(
            elevation=2,
            color=ft.colors.with_opacity(0.0, ft.colors.TRANSPARENT),
            disabled=self.disabled,
            scale= ft.transform.Scale(scale=0.97),
            animate_scale=ft.animation.Animation(600, ft.AnimationCurve.BOUNCE_OUT),
            col={"sm": 12, "md": 6, "xl": 6},
            content=ft.Container(
                border_radius=10,
                data=self.route,
                on_click=method_redirect,
                ink=True,
                bgcolor=ft.colors.with_opacity(0.0, ft.colors.TRANSPARENT),
                on_hover=self.hover,
                content=
                    ft.ListTile(
                        height=110,
                        leading=ft.Icon(self.icon,size=58,color=self.icon_color),
                        title=ft.Text(self.title,size=22,weight=ft.FontWeight.W_300),
                        subtitle=ft.Text(self.description,size=13)
                    )
            )
        )
        return self.card
    
    def hover(self,e:ft.ControlEvent) -> None:
        if e.data == "true":
            self.card.scale = 1.03
        else:
            self.card.scale = 0.97
        self.page.update()