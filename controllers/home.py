from flet_mvc import FletController
import ctypes


class HomeController(FletController):
    
    def get_name_user(self) -> str:
        size = ctypes.pointer(ctypes.c_ulong(0))
        ctypes.windll.secur32.GetUserNameExW(3, None, size)
        buffer = ctypes.create_unicode_buffer(size.contents.value)
        ctypes.windll.secur32.GetUserNameExW(3, buffer, size)
        full_name = buffer.value
        return full_name


    def navigate_secundary(self, e):
        print(self.model.example_title())
        """Example route change"""
        self.page.go("/secundary")
