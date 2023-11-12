import json
import os
import subprocess
import flet as ft
from threading import Thread
from flet_mvc import FletController

class WorkToolsController(FletController):
    def responsive_cards(self,card:dict) -> ft.Container:
        return ft.Container(
            col={"sm": 6, "md": 4, "xl": 3},
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Card(
                                content=ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.ListTile(
                                                width=230,
                                                height=50,
                                                leading=ft.Icon(card.get('tool_icon'), size=25, color=card.get('tool_color')),
                                                title=ft.Text(card.get('tool_title'), size=14, weight=ft.FontWeight.W_400),
                                            ),
                                        ]
                                    ),
                                    width=230,
                                ),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.ResponsiveRow(
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        controls=[ ft.Container(
                            col={"sm": 10, "md": 7, "xl": 3},
                            content=ft.TextButton(
                                content=ft.Row(
                                    [
                                        ft.Icon(card.get('tool_icon'), size=18, color=card.get('tool_color')),
                                        ft.Text(enviro.get('tool_enviroment_title'), size=15,weight=ft.FontWeight.W_400,color=ft.colors.ON_SURFACE)
                                    ]
                                ),
                                data=enviro.get('tool_enviroment_script'),
                                on_click=self.threading_proccess_bat,
                                disabled=enviro.get('tool_enviroment_disabled'),
                            )
                        ) for enviro in card.get('tool_list')]
                    )
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
        data = e.control.data
        thread = Thread(target=self.proccess_bat, args=(data,))
        thread.start()

    def proccess_bat(self, data:str) -> None:
        if os.path.exists(os.environ.get('userprofile')+fR"\Desktop\Configs\bats\{data}"):
            subprocess.call(
                [os.environ.get('userprofile')+fR"\Desktop\Configs\bats\{data}"])
        else:
            self.error_bat(data)

    def worktools_read_cards(self, responsive_row : ft.ResponsiveRow) -> None:
        cards = self.model.worktools_card_content("worktools-content")
        for n,card in enumerate(cards,1):
            if n == 7:
                responsive_row.controls.clear()
                self.error_card_enviroments()
                break
            else:
                responsive_row.controls.append(self.responsive_cards(card))
    
    def error_card_enviroments(self) -> None:
        error_enviroment = ft.AlertDialog(
            title=ft.Text("Error de Herramientas de trabajo"),
            content=ft.Text("No se ha podido acceder cargar correctamente a las Herramientas de trabajo ,por favor verifique e intentelo nuevamente."),
        )
        self.page.dialog = error_enviroment
        error_enviroment.open = True
        self._update()
        
    def error_bat(self, data:str) -> None:
        error_bat = ft.AlertDialog(
            title=ft.Text("Error de Archivo .bat"),
            content=ft.Text(f'No se encuentra el archivo "{data}" en la carpeta "bats"'),
        )
        self.page.dialog = error_bat
        error_bat.open = True
        self._update()

    def _update(self) -> None:
        self.page.update()