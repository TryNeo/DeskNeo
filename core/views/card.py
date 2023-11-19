import flet as ft

class Card:
    def __init__(self, **kwargs):
        self._card_title  = kwargs.get("card_title",'Title card')
        self._card_body = kwargs.get("card_body",'Body card')
        self._card_icon = kwargs.get("card_icon",None)
        self._card_icon_color = kwargs.get("card_icon_color",None)
        self._card_route  = kwargs.get("card_route",None)
        self._card_disabled = kwargs.get("card_disabled", False)

    def build(self) -> ft.Card:
        return ft.Card(
            elevation=2,
            color=ft.colors.with_opacity(0.0, ft.colors.TRANSPARENT),
            disabled=self._card_disabled,
            col={"sm": 12, "md": 6, "xl": 6},
            content=ft.Container(
                border_radius=10,
                on_click=self._card_route,
                ink=True,
                bgcolor=ft.colors.with_opacity(0.0, ft.colors.TRANSPARENT),
                content=ft.ListTile(
                            width=520,
                            height=110,
                            leading=self._icon_card(),
                            title=self._title_card(),
                            subtitle=self._subtitle_card(),
                        )
            )
        )
    
    def _icon_card(self) -> ft.Icon:
        return ft.Icon(self._card_icon,size=55,color=self._card_icon_color)
    
    def _title_card(self) -> ft.Text:
        return ft.Text(self._card_title,size=20,weight=ft.FontWeight.W_300)
    
    def _subtitle_card(self) -> ft.Text:
        return ft.Text(self._card_body,size=13)
        