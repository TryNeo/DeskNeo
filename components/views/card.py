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
            disabled=self._card_disabled,
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            width=520,
                            height=200,
                            leading=self._icon_card(),
                            title=self._title_card(),
                            subtitle=self._subtitle_card(),
                            on_click=self._card_route,
                        ),
                    ]
                )
            )
        )
    
    def _icon_card(self) -> ft.Icon:
        return ft.Icon(self._card_icon,size=55,color=self._card_icon_color)
    
    def _title_card(self) -> ft.Text:
        return ft.Text(self._card_title,size=15,weight=ft.FontWeight.W_300)
    
    def _subtitle_card(self) -> ft.Text:
        return ft.Text(self._card_body)