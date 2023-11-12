import ctypes
import json
import os
import flet as ft
from flet_mvc import FletController
from core.views.card import Card
from typing import Type

class HomeController(FletController):
    def get_name_user(self) -> str:
        size = ctypes.pointer(ctypes.c_ulong(0))
        ctypes.windll.secur32.GetUserNameExW(3, None, size)
        buffer = ctypes.create_unicode_buffer(size.contents.value)
        ctypes.windll.secur32.GetUserNameExW(3, buffer, size)
        full_name = buffer.value
        return full_name
    

    def responsive_cards(self,responsive_row:ft.ResponsiveRow,controller: Type[FletController]) -> None:
        cards = self.model.home_cards_content("cards-content")
        for card in cards:
            if hasattr(controller,card.get('card_route')):
                try:
                    card_route = getattr(controller,card.get('card_route'))
                except Exception as e:
                    card_route = self.error_method
            else:
                card_route = self.error_method
            responsive_row.controls.append(
                Card(
                    card_title=card.get('card_title'),
                    card_body=card.get('card_body'),
                    card_icon=card.get('card_icon'),
                    card_icon_color=card.get('card_icon_color'),
                    card_route=card_route,
                    card_disabled=card.get('card_disabled'),
                    controller=self.page,
                ).build()
            )


    def read_file_json(self, path: str) -> dict:
        try:
            with open(path, 'r',encoding='utf-8') as file:
                data = json.load(file,parse_constant=True)
                return data
        except (FileNotFoundError, PermissionError, IsADirectoryError, UnicodeDecodeError) as e:
            return self.model.home_card_default()



    def error_method(self,e:ft.ControlEvent) -> None:
        error_method = ft.AlertDialog(
                title=ft.Text("Error de configuración"),
                content=ft.Text("No se ha podido acceder al metodo,\npor favor verifique e intentelo nuevamente."),
            )
        self.page.dialog = error_method
        error_method.open = True
        self._update()

    def error_directory(self) -> None:
        error_directory = ft.AlertDialog(
                title=ft.Text("Error de directorio"),
                content=ft.Text("No se encuentra la carpeta 'Configs' en el escritorio"),
            )
        self.page.dialog = error_directory
        error_directory.open = True
        self._update()

    def route_worktools(self,e: ft.ControlEvent) -> None:
        if os.path.exists(os.environ.get('userprofile')+"\Desktop\Configs"):
            self.page.go('/work-tools')
            self._update
        else:
            self.error_directory

    def route_textopus(self,e: ft.ControlEvent) -> None:
        if os.path.exists(os.environ.get('userprofile')+"\Desktop\Configs"):
            self.page.go('/text-opus')
            self._update
        else:
            self.error_directory

    def route_checklist(self,e: ft.ControlEvent) -> None:
        if os.path.exists(os.environ.get('userprofile')+"\Desktop\Configs"):
            self.page.go('/checklist')
            self._update
        else:
            self.error_directory

    def _update(self) -> None:
        self.page.update()