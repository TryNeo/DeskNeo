from flet_mvc import FletModel, data
import flet as ft


class HomeModel(FletModel):
    def home_title(self, value: str) -> str:
        return f"Bienvenido a la aplicación - {value}"
    
    def home_cards(self):
        return [
            {
                'card_title': '--------------',
                'card_body' : '-----------------------------------',
                'card_icon' : ft.icons.EDIT_DOCUMENT,
                'card_color': ft.colors.LIME_600,
                'card_route': None,
                'card_disabled': False,
            },
        ]