import json
import os
import subprocess
import flet as ft
from threading import Thread
from flet_mvc import FletController

class WorkToolsController(FletController):
    def responsive_cards(self,wk:dict) -> ft.Container:
        return ft.Container(
            padding=5,
            col={"sm": 6, "md": 4, "xl": 4},
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Card(
                                elevation=3,
                                color=ft.colors.with_opacity(0.0, ft.colors.TRANSPARENT),
                                content=ft.Container(
                                    content=ft.ListTile(
                                        width=250,
                                        height=50,
                                        leading=ft.Icon(wk.get('icon'), size=25, color=wk.get('icon_color')),
                                        title=ft.Text(wk.get('title'), size=14, weight=ft.FontWeight.W_600),
                                    ),
                                    width=250,
                                ),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.ResponsiveRow(
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        controls=[ ft.Container(
                            content=ft.TextButton(
                                width=199,
                                content=ft.Row(
                                    [
                                        ft.Icon(wk.get('icon'), size=28, color=wk.get('icon_color')),
                                        ft.Text(enviro.get('name'), size=15,weight=ft.FontWeight.W_400,color=ft.colors.ON_SURFACE),
                                    ]
                                ),
                                data=enviro.get('script'),
                                on_click=self.threading_proccess_bat,
                                disabled=enviro.get('disabled'),
                            )
                        ) for enviro in wk.get('tool_list')]
                    ),
                ]
            )
        )

    def read_file_json(self, path: str) -> dict:
        try:
            with open(path, 'r',encoding='utf-8') as file:
                data = json.load(file,parse_constant=True)
                return data
        except (FileNotFoundError, PermissionError, IsADirectoryError, UnicodeDecodeError) as e:
            return self.model.worktools_card_default()

        
    def threading_proccess_bat(self,e:ft.ControlEvent) -> None:
        data  : str= e.control.data
        thread : Thread = Thread(target=self.proccess_bat, args=(data,))
        thread.start()

    def proccess_bat(self, data:str) -> None:
        if os.path.exists(os.environ.get('userprofile')+fR"\Desktop\Configs\bats\{data}"):
            subprocess.call(
                [os.environ.get('userprofile')+fR"\Desktop\Configs\bats\{data}"])
        else:
            self.error_bat(data)

    def worktools_read_cards(self, responsive_row : ft.ResponsiveRow) -> None:
        woktools : list[dict] = self.model.worktools_card_data()
        for wk in woktools:
            responsive_row.controls.append(self.responsive_cards(wk))
    
    def error_bat(self, data:str) -> None:
        error_bat : ft.AlertDialog = ft.AlertDialog(
            title=ft.Text("Error de Archivo .bat"),
            content=ft.Text(f'No se encuentra el archivo "{data}" en la carpeta "bats"'),
        )
        self.page.dialog : ft.AlertDialog = error_bat
        error_bat.open : bool = True
        self._update()

    def _update(self) -> None:
        self.page.update()