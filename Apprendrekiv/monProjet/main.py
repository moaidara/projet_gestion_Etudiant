from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label 
# from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from GestionnaireEcran import MonGestionnaireEcran

##Important: changer le chemin d'acces des fichiers CSV avant de lance l'interface graphique 
#Pour plus de details Aller sur le Fichier README.md

class GestionEcran(MonGestionnaireEcran):
    pass

class MainApp(App):
    # Propriété pour gérer l'écran principal de l'application
    gestion = ObjectProperty()
    def build(self):
        # Initialise l'écran principal en utilisant GestionEcran
        self.gestion = GestionEcran() 
        return self.gestion
    pass



app = MainApp()
app.run()


  
