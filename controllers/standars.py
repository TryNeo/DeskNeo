from flet_mvc import FletController
import flet as ft
import json
import os

class StandarsController(FletController):
    def standars_read_items_navs(self,navs: ft.NavigationDrawer) -> None:
        items = self.model.standars_navs("navigation-items-content")
        for item in items:
            if item.get('icon_name_on') == True and item.get('icon_content_on') == False:
                navs.controls.append(ft.Container(height=12))
                navs.controls.append(ft.NavigationDrawerDestination(
                    label=item.get('label_name'),
                    icon=item.get('icon_name'),
                ))
            if item.get('icon_name_on') == False and item.get('icon_content_on') == True:
                navs.controls.append(ft.Container(height=12))
                navs.controls.append(ft.NavigationDrawerDestination(
                    label=item.get('label_name'),
                    icon_content=ft.Image(src=f"/icons/{item.get('icon_content')}.svg", width=20, height=20, color=ft.colors.ON_SURFACE),
                ))

    def read_file_json(self, path: str) -> dict:
        try:
            with open(path, 'r',encoding='utf-8') as file:
                data = json.load(file,parse_constant=True)
                return data
        except (FileNotFoundError, PermissionError, IsADirectoryError, UnicodeDecodeError) as e:
            return self.model.standars_navs_default()

    def select_page(self,pages : list,navigation: ft.NavigationDrawer) -> None:
        for p in range(len(pages)):
            pages[p].visible = True if p ==  navigation.selected_index else False
        self._update()

    def dest_change(self,e: ft.ControlEvent) -> None:
        self.select_page(e.control.data,e.control)

    def _update(self) -> None:
        self.page.update()