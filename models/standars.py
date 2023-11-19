from flet_mvc import FletModel
import flet as ft
import os

class StandarsModel(FletModel):
    def standars_title(self):
        return "Concepto y estándares generales"
    
    def standars_navs_default(self) -> list[dict]:
        return [{}]

    def standars_navs(self,path: str) -> dict:
        if  os.path.exists(os.environ.get('userprofile')+"\Desktop\Configs\data"):
            items = self.controller.read_file_json(os.environ.get('userprofile')+f"\Desktop\Configs\data\{path}.json")
            return items
        else:
            self.standars_navs_default()