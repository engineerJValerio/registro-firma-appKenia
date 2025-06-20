from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class TestApp(MDApp):
    def build(self):
        return MDLabel(text="¡Hola, esta es una prueba!", halign="center")

TestApp().run()
