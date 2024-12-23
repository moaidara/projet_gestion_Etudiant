# Les importations 
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

# Permet de prendre en compte les modifications faites dans le code kivy 
Builder.load_file("modifier.kv")        

# Creation d'une classe
class Modifier(BoxLayout):
    def validate_inputs(self):
        matricule_value = self.ids.matricule.text.strip()
        is_enabled = bool(matricule_value)
        #Activation / desactivation des champs dpuis le code modify.kv
        self.ids.nom.disabled = not is_enabled
        self.ids.prenom.disabled = not is_enabled
        self.ids.age.disabled = not is_enabled
        self.ids.niveau.disabled = not is_enabled
        self.ids.adresse.disabled = not is_enabled
        self.ids.sex.disabled = not is_enabled
        self.ids.nom_users.disabled = not is_enabled
        self.ids.numero.disabled = not is_enabled
        self.ids.mail.disabled = not is_enabled 
    pass
