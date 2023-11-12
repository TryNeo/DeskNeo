from flet_mvc import FletModel, data
import flet as ft
import os

class WorkToolsModel(FletModel):
    def worktools_title(self):
        return "Herramientas de trabajo"

    def worktools_card_default(self) -> list[dict]:
        return [{}]

    def worktools_card_content(self,path: str) -> dict:
        if  os.path.exists(os.environ.get('userprofile')+"\Desktop\Configs\data"):
            card = self.controller.read_file_json(os.environ.get('userprofile')+f"\Desktop\Configs\data\{path}.json")
            return card
        else:
            self.worktools_card_default()