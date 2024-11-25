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
# print(etudiant2.nom)

#Creation d'un tableau
tableau_Etudiant = [
    [etudiant2.nom, etudiant2.prenom, etudiant2.nom_users, etudiant2.matricule, etudiant2.age, etudiant2.adresse, etudiant2.niveau]
]


#Creation d'un dataframe
tableau_dataframe = pd.DataFrame(tableau_Etudiant, columns=['Nom', 'Prenom', 'nom_users', 'Matricule', 'Age', 'Adresse', 'niveau'])

#Afficher le dataframe
# print(tableau_dataframe['Matricule'])

#Fonction Ajouter un Etudiant

def Ajout_Etudiant():
#importer les variables global dans la fonction pour eviter une confusion
    global tableau_Etudiant
    global tableau_dataframe
#Recolter les information d'un etudiant
    nom=input('Donnez le nom: ')
    prenom=input('Donnez le prenom: ')
    age=int(input('Donnez l age: '))
    adresse=input('Donnez l adresse: ')
    niveau=input('Donnez le niveau: ')
    nom_users=input('Donnez le nom d utilisateur: ')
    matricule=int(input('Donnez le matricule: '))
#Creer une nouvelle instance de la classe Etudiant    
    etudiant = Etudiant(nom, prenom, nom_users, matricule, age, adresse, niveau)
#Ajouter dans le tableau
    tableau_Etudiant.append([etudiant.nom, etudiant.prenom, etudiant.nom_users, etudiant.matricule, etudiant.age, etudiant.adresse, etudiant.niveau])
#Mettre a jour le DataFrame   
    tableau_dataframe = pd.DataFrame(tableau_Etudiant, columns=['Nom', 'Prenom', 'nom_users', 'Matricule', 'Age', 'Adresse', 'niveau'])


    #Ajouts de nouvelles fontionalites...

# Fonction pour supprimer un étudiant par matricule
def Supprimer_Etudiant():
    global tableau_Etudiant
    global tableau_dataframe
    matricule = int(input("Entrez le matricule de l'étudiant à supprimer: "))
    # Trouver l'index de l'étudiant dans le tableau
    index_a_supprimer = next((index for index, etudiant in enumerate(tableau_Etudiant) if etudiant[3] == matricule), None)
    if index_a_supprimer is not None:
        tableau_Etudiant.pop(index_a_supprimer)
        tableau_dataframe = pd.DataFrame(tableau_Etudiant, columns=['Nom', 'Prenom', 'nom_users', 'Matricule', 'Age', 'Adresse', 'niveau'])
        print("Étudiant supprimé avec succès.")
    else:
        print("Aucun étudiant trouvé avec ce matricule.")



# Fonction pour rechercher et afficher un étudiant par matricule
def Rechercher_Etudiant():
    matricule = int(input("Entrez le matricule de l'étudiant à rechercher: "))
    # Rechercher l'étudiant dans le tableau
    etudiant = next((et for et in tableau_Etudiant if et[3] == matricule), None)
    if etudiant:
        etudiant_df = pd.DataFrame([etudiant], columns=['Nom', 'Prenom', 'nom_users', 'Matricule', 'Age', 'Adresse', 'niveau'])
        print("Étudiant trouvé:")
        print(etudiant_df)
    else:
        print("Aucun étudiant trouvé avec ce matricule.")

#test
# Ajout_Etudiant()
# print(tableau_dataframe)
# Supprimer_Etudiant()
# Rechercher_Etudiant()