from flet_mvc import FletModel, data
import flet as ft


class HomeModel(FletModel):
    def home_title(self, value: str) -> str:
        return f"Bienvenido a la aplicación - {value}"