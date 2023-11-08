import ctypes
import json
import os
import flet as ft
from flet_mvc import FletController

class HomeController(FletController):
    def get_name_user(self) -> str:
        size = ctypes.pointer(ctypes.c_ulong(0))
        ctypes.windll.secur32.GetUserNameExW(3, None, size)
        buffer = ctypes.create_unicode_buffer(size.contents.value)
        ctypes.windll.secur32.GetUserNameExW(3, buffer, size)
        full_name = buffer.value
        return full_name
    
    def read_file_json(self, path: str) -> dict:
        try:
            with open(path, 'r',encoding='utf-8') as file:
                data = json.load(file,parse_constant=True)
                return data
        except (FileNotFoundError, PermissionError, IsADirectoryError, UnicodeDecodeError) as e:
            return self.model.home_card_default()

    def _update(self) -> None:
        self.page.update()

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

    def route_utilities(self,e: ft.ControlEvent) -> None:
        if os.path.exists(os.environ.get('userprofile')+"\Desktop\Configs"):
            self.page.go('/utilidades')
            self._update
        else:
            self.error_directory

    def route_checklist(self,e: ft.ControlEvent) -> None:
        if os.path.exists(os.environ.get('userprofile')+"\Desktop\Configs"):
            self.page.go('/checklist')
            self._update
        else:
            self.error_directory