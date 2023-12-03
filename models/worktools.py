import os
import flet as ft
from flet_mvc import FletModel, data
from utils.readyamlfile import ReadYamlFile

class WorkToolsModel(FletModel):
    def worktools_title(self):
        return "Herramientas de trabajo"

    def worktools_card_default(self) -> list[dict]:
        return [
            {}
        ]
    
    def worktools_card_data(self) -> list[dict]:
        try:
            return ReadYamlFile("worktools","yaml").read()
        except Exception as e:
            return self.worktools_card_default()
