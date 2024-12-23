from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file('ajout.kv')

class Ajout(BoxLayout):
    pass

# class MainApp(App):
#     def build(self):
#         return Ajout()
#     pass
# app=MainApp()
# app.run()