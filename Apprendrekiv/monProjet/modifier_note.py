from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file("modifier_note.kv")

class Modifier_note(BoxLayout):
    def validate_inputs(self):
        matricule_value = self.ids.matricule.text.strip()
        is_enabled      = bool(matricule_value)

        # Activation/Desactivation des champs pour la matiere anglais
        self.ids.matiere.disabled = not is_enabled
        

        # Activation/Desactivation des champs pour les notes
        self.ids.devoir.disabled = not is_enabled
        self.ids.exam.disabled     = not is_enabled




