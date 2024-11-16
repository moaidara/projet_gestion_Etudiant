import pandas as pd

#creation d'un objet etudiant avec ses propriete 
class Etudiant:
    def __init__(self, nom, prenom, nom_users, matricule, age, adresse, niveau):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.adresse = adresse
        self.niveau = niveau
        self.nom_users = nom_users
        self.matricule = matricule
    
    
        
            
#test
etudiant2 = Etudiant('Mansour', 'Aidara', 'aidara300', 1234565, 21, 'Medina', 'l2')
print(etudiant2.nom)

#Creation d'un tableau
tableau_Etudiant = [
    [etudiant2.nom, etudiant2.prenom, etudiant2.nom_users, etudiant2.matricule, etudiant2.age, etudiant2.adresse, etudiant2.niveau]
]


#Creation d'un dataframe
# tableau_dataframe = pd.DataFrame(tableau_Etudiant, columns=['Nom', 'Prenom', 'nom_users', 'Matricule', 'Age', 'Adresse', 'niveau'])

#Afficher le dataframe
# print(tableau_dataframe['Matricule'])