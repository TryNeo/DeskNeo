import os
import flet as ft
from typing import Type
from flet_mvc import FletController

class Markdown:
    def __init__(self,title_markdown:str=None,content_markdown:str =None,controller:Type[FletController]=None,key_markdown:str=""):
        self.title_markdown = title_markdown
        self.content_markdown = content_markdown
        self.controller = controller
        self.key_markdown = key_markdown

    def main(self) -> ft.Container:
        return ft.Container(
            content=ft.Column(
                controls=[
                    self.head_main(),
                    self.body_main(),
                ],
            ),
            key=self.key_markdown,
        )

    def head_main(self) -> ft.Card:
        return ft.Column(
            [
                ft.Card(
                    elevation=3,
                    content=ft.Container(
                        ft.Text(self.title_markdown, size=21,weight=ft.FontWeight.W_300),
                        padding=8,
                    ),
                    color=ft.colors.with_opacity(0.0, ft.colors.TRANSPARENT),
                )
            ],
            horizontal_alignment="stretch",
        )
    
    def body_main(self) -> ft.Markdown:
        return ft.Markdown(
            value=f"""{self.read_md(self.content_markdown)}""",
            selectable=True,
            extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
            code_theme="dracula",
        )

    def comand_gif(self,gif:str='') -> ft.Container:
        comand_gif_markdown = ft.Column(
            controls=[
                ft.Markdown(
                    value=f"""{self.read_md(self.content_markdown)}""",
                    selectable=True,
                    extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
                    code_theme="dracula",
                ),
                ft.Row([
                    ft.Text('ver ejecucion del comando:',size=15,weight=ft.FontWeight.W_100,color=ft.colors.ON_SURFACE),
                    ft.TextButton(
                        data=[f"![Test gif]({gif})",False],
                        on_click=self.change_visible_gif,
                        content=ft.Image(src=f"/icons/eye.svg", width=20, height=20, color=ft.colors.ON_SURFACE)
                    ),
                ]),
            ]
        )
        content_comand_gif = comand_gif_markdown
        comand_gif_markdown.controls[1].controls[1].key = content_comand_gif
        return ft.Container(
            content=comand_gif_markdown
        )
    
    def change_visible_gif(self,e):
        visible = not e.control.data[1]
        e.control.data[1] = visible
        if visible:
            e.control.content = ft.Image(src=f"/icons/eye-off.svg", width=20, height=20, color=ft.colors.ON_SURFACE)
            markdown_default= ft.Markdown(
                value=f"""{e.control.data[0]}""",
            )
            e.control.key.controls.append(markdown_default)
        else:
            e.control.content = ft.Image(src=f"/icons/eye.svg", width=20, height=20, color=ft.colors.ON_SURFACE)
            e.control.key.controls.pop()
        self.controller.page.update()

    def read_md(self,archivo_md : str):
        try:
            with open(os.environ.get('userprofile')+R"\Desktop\Configs\markdown"+f"\{archivo_md}", "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
                return contenido
        except FileNotFoundError:
            return ""
