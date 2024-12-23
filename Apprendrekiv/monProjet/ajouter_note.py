from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file("ajouter_note.kv")

class Ajouter_note(BoxLayout):
    # def validate_inputs(self):
    #     matricule_value = self.ids.matricule.text.strip()
    #     is_enabled      = bool(matricule_value)

    #     # Activation/Desactivation des champs pour la matiere anglais
    #     self.ids.anglais_devoir.disabled = not is_enabled
    #     self.ids.anglais_exam.disabled = not is_enabled
    #     self.ids.probabilite_devoir.disabled = not is_enabled
    #     self.ids.probabilite_exam.disabled = not is_enabled
    #     self.ids.java_devoir.disabled = not is_enabled
    #     self.ids.java_exam.disabled = not is_enabled
    #     self.ids.algo_devoir.disabled = not is_enabled
    #     self.ids.algo_exam.disabled = not is_enabled
    #     self.ids.reseau_devoir.disabled = not is_enabled
    #     self.ids.reseau_exam.disabled = not is_enabled  

    #     # Activation/Desactivation des champs pour les notes
    #     self.ids.devoir.disabled = not is_enabled
    #     self.ids.exam.disabled     = not is_enabled
    pass
# class MyApp(App):
#     def build (self):
#         # Instancie et retourne le widget principal
#         return ajouter_note()
# if __name__ == "__main__":
#     MyApp().run()
