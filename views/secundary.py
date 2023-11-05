from flet_mvc import FletView
import flet as ft


class SecundaryView(FletView):
    def __init__(self, controller, model,url):
        self.url = url
        view = ft.View(
            route=url,
            controls=[
                ft.Text(ref=model.example_title, size=30),
                ft.ElevatedButton("Go to home", on_click=controller.return_home),
            ]
        )
        super().__init__(model, view, controller)