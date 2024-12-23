from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
import pandas as pd
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from codePython import monCode


Builder.load_file("acceuil.kv")

class Acceuil(BoxLayout):  
    pass

class MonTableau(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.last_tableau=None
        self.Affiche_tableau()
        Clock.schedule_interval(self.verifier_misAjour, 1)

    def Affiche_tableau(self):
        tableau=monCode.Importation()
        # tableau=code.tableau_dataframe
        self.last_tableau=tableau.copy()
        for column in tableau.columns:
            self.add_widget(Label(text=f"[b]{column}[/b]", markup=True, size_hint_y=None, height=40))

        for _, row in tableau.iterrows():
            for cell in row:
                self.add_widget(Label(text=str(cell), size_hint_y=None, height=50))
    def MettreAJour(self):
        self.clear_widgets()
        self.Affiche_tableau()

    def verifier_misAjour(self, dt):
        tableau=monCode.Importation()
        if not tableau.equals(self.last_tableau):
            self.MettreAJour()
    pass

