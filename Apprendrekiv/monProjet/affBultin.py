from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from codePython import monCode
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
Builder.load_file("affBultin.kv")

class AffBultin(BoxLayout):
    pass

class MainApp(App):
    pass

class MonBultin(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.last_tableau = None
        self.Afficher_Bultin()
        Clock.schedule_interval(self.verifier_misAjour, 1)
    
    
    def Afficher_Bultin(self):
        Tableau_Bultin = monCode.Importation_Note('Bultin')
        self.last_tableau= Tableau_Bultin.copy()
        for column in Tableau_Bultin:
            self.add_widget(Label(text=f"[b]{column}[/b]", markup=True, size_hint_y=None, height=40))
        
        for _, row in Tableau_Bultin.iterrows():
            for cell in row:
                self.add_widget(Label(text=str(cell), size_hint_y=None, height=50))

    def MettreAJour(self):
        self.clear_widgets()
        self.Afficher_Bultin()

    def verifier_misAjour(self, dt):
        tableau=monCode.Importation_Note('Bultin')
        if not tableau.equals(self.last_tableau):
            self.MettreAJour()



