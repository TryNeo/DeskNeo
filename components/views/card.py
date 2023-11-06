import flet as ft

class Card:
    def __init__(self, **kwargs):
        self._card_title  = kwargs.get("card_title",'Title card')
        self._card_body = kwargs.get("card_body",'Body card')
        self._card_icon = kwargs.get("card_icon",None)
        self._card_icon_color = kwargs.get("card_icon_color",None)
        self._card_route  = kwargs.get("route_view",None)
        self._card_disabled = kwargs.get("card_disabled", False)

    def build(self) -> ft.Card:
        return ft.Card(
            content=ft.ListTile(
                leading=self._icon_card(),
                title=self._title_card(),
                subtitle=self._subtitle_card(),
                on_click=self._card_route,
            ),
            disabled=self._card_disabled,
        )
    
    def _icon_card(self) -> ft.Icon:
        return ft.Icon(self._card_icon,size=50,color=self._card_icon_color)
    
    def _title_card(self) -> ft.Text:
        return ft.Text(self._card_title,size=15,weight=ft.FontWeight.W_300)
    
    def _subtitle_card(self) -> ft.Text:
        return ft.Text(self._card_body)