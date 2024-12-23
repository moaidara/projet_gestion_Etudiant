from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file("test.kv")



class Test(BoxLayout):
    pass


# class MainApp(App):
#     def build(self):
#         return Test()
#     pass
# app=MainApp()
# app.run()
