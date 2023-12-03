import os
import ctypes
import flet as ft
from typing import Type
from utils.card import Card
from flet_mvc import FletController
class HomeController(FletController):
    def get_name_user(self) -> str:
        size = ctypes.pointer(ctypes.c_ulong(0))
        ctypes.windll.secur32.GetUserNameExW(3, None, size)
        buffer = ctypes.create_unicode_buffer(size.contents.value)
        ctypes.windll.secur32.GetUserNameExW(3, buffer, size)
        full_name = buffer.value
        return full_name

    def responsive_cards(self,responsive_row:ft.ResponsiveRow) -> None:
        cards : list = self.model.home_card_data()
        if len(cards) == 0:
            cards : list = self.model.home_card_default()
        for card in cards:
        #-------------------------------------------------------------------------|
        # NO TOMAR EN CUENTA ESTE CODIGO
        #    if hasattr(controller,card.get('card_route')):                    
        #        try:
        #            card_route = getattr(controller,card.get('card_route'))
        #        except Exception as e:
        #            card_route = self.error_method
        #    else:
        #        card_route = self.error_method
        #-----------------------------------------------------------------------|
            responsive_row.controls.append(
                Card(
                    page=self.page,
                    title=card.get('title'),
                    description=card.get('description'),
                    icon=card.get('icon'),
                    icon_color=card.get('color_icon'),
                    route=card.get('route'),
                    disabled=card.get('disabled'),
                ).build(self.route_card)
            )

    def route_card(self,e: ft.ControlEvent) -> None:
        if os.path.exists(os.environ.get('userprofile')+"\Desktop\Configs"):
            self.page.go(f'/{e.control.data}')
            self._update
        else:
            self.error_directory

    def error_directory(self) -> None:
        error_directory = ft.AlertDialog(
                title=ft.Text("Error de directorio"),
                content=ft.Text("No se encuentra la carpeta 'Configs' en el escritorio"),
            )
        self.page.dialog = error_directory
        error_directory.open = True
        self._update()

    def _update(self) -> None:
        self.page.update()
