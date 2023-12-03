import os
import flet as ft
from flet_mvc import FletModel
from utils.readyamlfile import ReadYamlFile

class HomeModel(FletModel):    
    def home_title(self) -> str:
        return f"Bienvenido - {self.controller.get_name_user()}"
    
    def home_card_default(self) -> list[dict]:
        return [{   'title': 'No existe el archivo cards.yml',
            'description' : f'No existe informacion o el archivo en la ruta {os.environ.get("userprofile")}\Desktop\Configs\yaml\cards.yml',
            'icon' : ft.icons.ATTACH_FILE,
            'icon_color': ft.colors.LIGHT_BLUE_300,
            'route': None,
            'disabled': False,
        }]
    
    def home_card_data(self) -> list[dict]:
        try:
            return ReadYamlFile("cards","yaml").read()
        except Exception as e:
            return self.home_card_default()