import os
import flet as ft
from flet_mvc import FletModel, data

class HomeModel(FletModel):
    def home_title(self, value: str) -> str:
        return f"Bienvenido - {value}"
    
    def home_card_default(self) -> list[dict]:
        return [{
            'card_title': 'Titulo por defecto',
            'card_body' : 'No existe el archivo en la ruta \Configs\data\cards-content.json',
            'card_icon' : ft.icons.ATTACH_FILE,
            'card_icon_color': ft.colors.LIGHT_BLUE_300,
            'card_route': None,
            'card_disabled': False,
        }]
    
    def home_cards_content(self,path: str) -> dict:
        if  os.path.exists(os.environ.get('userprofile')+"\Desktop\Configs\data"):
            card = self.controller.read_file_json(os.environ.get('userprofile')+f"\Desktop\Configs\data\{path}.json")
            return card
        else:
            return self.home_card_default()