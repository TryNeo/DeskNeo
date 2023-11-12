from flet_mvc import FletController
import flet as ft
import os
import datetime

class TextOpusController(FletController):
    fecha_actual = datetime.date.today()
    nombre_fichero=f"nota_{fecha_actual.strftime('%Y-%m-%d')}.txt"
    ruta_fichero = os.path.join(os.environ.get('userprofile')+R"\Desktop\Configs\notes",nombre_fichero)

    def save_textopus(self,e:ft.ControlEvent) -> None:
        try:
            with open(self.ruta_fichero, 'w',encoding='utf-8') as file:
                file.write(e.control.value)
        except (FileNotFoundError, PermissionError, IsADirectoryError, UnicodeDecodeError) as e:
            return 'Bienvenido a TextOpus'

    def read_textopus(self) -> str | None:
        try:
            with open(self.ruta_fichero, 'r',encoding='utf-8') as file:
                return file.read()
        except (FileNotFoundError, PermissionError, IsADirectoryError, UnicodeDecodeError) as e:
            return 'Bienvenido a TextOpus'