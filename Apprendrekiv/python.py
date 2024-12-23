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
#Mettre a jour le DataFrame(tableau d'etudiant)   
    tableau_dataframe = pd.DataFrame(tableau_Etudiant, columns=['Nom', 'Prenom', 'nom_users', 'Matricule', 'Age', 'Adresse', 'niveau'])


# Fonction pour supprimer un étudiant par matricule
def Supprimer_Etudiant():
    global tableau_Etudiant
    global tableau_dataframe
    matricule = int(input("Entrez le matricule de l'étudiant à supprimer: "))
    # Trouver l'index de l'étudiant dans le tableau(son matricule)
    index_a_supprimer = next((index for index, etudiant in enumerate(tableau_Etudiant) if etudiant[3] == matricule), None)
    if index_a_supprimer is not None:
        tableau_Etudiant.pop(index_a_supprimer)
        tableau_dataframe = pd.DataFrame(tableau_Etudiant, columns=['Nom', 'Prenom', 'nom_users', 'Matricule', 'Age', 'Adresse', 'niveau'])
        print("Étudiant supprimé avec succès.")
    else:
        print("Aucun étudiant trouvé avec ce matricule.")



# Fonction pour rechercher et afficher un étudiant par matricule
def Rechercher_Etudiant(matricule):
    # Rechercher l'étudiant dans le tableau
    etudiant = next((et for et in tableau_Etudiant if et[3] == matricule), None)
    if etudiant:
        etudiant_df = pd.DataFrame([etudiant], columns=['Nom', 'Prenom', 'nom_users', 'Matricule', 'Age', 'Adresse', 'niveau'])
        print("Étudiant trouvé:")
        print(etudiant_df)
    else:
        print("Aucun étudiant trouvé avec ce matricule.")


# Dictionnaire pour stocker les notes des étudiants
notes_etudiants = {}

# Fonction pour récupérer les notes d'un étudiant
def Recuperer_Notes(matricule):
    """
    Ajoute des notes pour un étudiant identifié par son matricule.
    Les notes sont stockées dans le dictionnaire 'notes_etudiants'.
    """
    global notes_etudiants 
    if matricule in tableau_dataframe['Matricule'].values:
        notes = input("Entrez les notes de l'étudiant séparées par des espaces : ")
        # Transformer les notes en liste de nombres
        notes_etudiants[matricule] = list(map(float, notes.split()))
        print("Notes ajoutées avec succès.")
    else:
        print("Matricule introuvable.")
def Authentification(nom, matricule):
    """
    Vérifie si un étudiant avec le nom et le matricule donnés existe dans le DataFrame.
    Retourne True si trouvé, sinon False.
    """
    # Vérifie si une ligne du DataFrame correspond aux deux critères
    return ((tableau_dataframe['Nom'] == nom) & (tableau_dataframe['Matricule'] == matricule)).any()


# Fonction pour calculer la moyenne d'un étudiant

def calculer_moyenne(matricule):
    if matricule in notes_etudiants:
        return sum(notes_etudiants[matricule]) / len(notes_etudiants[matricule])
    else:
        return None
#mis a jour du dataframe
tableau_dataframe['Moyenne'] = tableau_dataframe['Matricule'].apply(calculer_moyenne)    

#fonction classement des etudiants
def Classement_Etudiants():
    """
    Affiche un classement des étudiants basé sur leur moyenne.
    """
    moyennes = []
    for matricule, notes in notes_etudiants.items():
        moyenne = sum(notes) / len(notes)
        nom = tableau_dataframe.loc[tableau_dataframe['Matricule'] == matricule, 'Nom'].values[0]
        moyennes.append((nom, moyenne))
    
    classement = sorted(moyennes, key=lambda x: x[1], reverse=True)
    print("Classement des étudiants :")
    for i, (nom, moyenne) in enumerate(classement, start=1):
        print(f"{i}. {nom} - {moyenne:.2f}")


#fonction qui permet de notifier l'etudiant de sa moyenne
def Notifier_Etudiants(seuil=10):
    """
    Notifie les étudiants avec une moyenne en dessous du seuil.
    """
    for matricule, notes in notes_etudiants.items():
        moyenne = sum(notes) / len(notes)
        if moyenne < seuil:
            nom = tableau_dataframe.loc[tableau_dataframe['Matricule'] == matricule, 'Nom'].values[0]
            print(f"Notification : {nom}, votre moyenne ({moyenne:.2f}) est inférieure au seuil de {seuil}.")

#fonction pour enregistrer les absences
absences_etudiants = {}

def Ajouter_Absence(matricule, matiere):
    """
    Ajoute une absence pour un étudiant dans une matière donnée.
    """
    if matricule not in absences_etudiants:
        absences_etudiants[matricule] = {}
    if matiere not in absences_etudiants[matricule]:
        absences_etudiants[matricule][matiere] = 0
    absences_etudiants[matricule][matiere] += 1
    print(f"Absence ajoutée pour {matiere}. Total : {absences_etudiants[matricule][matiere]}.")

def Afficher_Absences(matricule):
    """
    Affiche les absences d'un étudiant par matière.
    """
    if matricule in absences_etudiants:
        print(f"Absences pour l'étudiant {matricule} :")
        for matiere, absences in absences_etudiants[matricule].items():
            print(f"{matiere}: {absences} absences")
    else:
        print("Aucune absence enregistrée pour cet étudiant.")


#afficher les bulletins

def Generer_Bulletin_DataFrame():
    global tableau_dataframe  # On met à jour le DataFrame existant
    matieres = ["Mathématiques", "Physique", "Chimie", "Biologie"]  # Exemple de matières
    if not tableau_Etudiant:
        print("Aucun étudiant enregistré.")
        return None

    if not notes_etudiants:
        print("Aucune note enregistrée.")
        return None

    # Liste pour stocker les données des bulletins
    bulletin_data = []
    total_notes = []  # Pour calculer la moyenne générale de la classe

    for etudiant in tableau_Etudiant:
        matricule = etudiant[3]  # Récupérer le matricule
        nom, prenom = etudiant[0], etudiant[1]
        niveau = etudiant[6]

        # Récupérer les notes
        notes = notes_etudiants.get(matricule, ["N/A"] * len(matieres))
        moyenne_etudiant = sum(notes) / len(notes) if isinstance(notes[0], (int, float)) else "N/A"

        # Ajouter les données au tableau
        bulletin_data.append({
            "Nom": nom,
            "Prenom": prenom,
            "Matricule": matricule,
            "Niveau": niveau,
            **{matiere: notes[i] if i < len(notes) else "N/A" for i, matiere in enumerate(matieres)},
            "Moyenne Individuelle": moyenne_etudiant
        })

        # Ajouter les notes au calcul de la moyenne générale si elles sont valides
        if isinstance(moyenne_etudiant, (int, float)):
            total_notes.extend(notes)

    # Calcul de la moyenne générale de la classe
    moyenne_generale = sum(total_notes) / len(total_notes) if total_notes else "N/A"

    # Mettre à jour le DataFrame existant
    tableau_dataframe = pd.DataFrame(bulletin_data)

    print("\n--- Moyenne Générale de la Classe ---")
    print(f"Moyenne Générale : {moyenne_generale:.2f}" if isinstance(moyenne_generale, (int, float)) else "Non calculable")
    
    # Ajouter la moyenne générale au DataFrame (colonne supplémentaire, si pertinent)
    tableau_dataframe["Moyenne Générale"] = moyenne_generale if isinstance(moyenne_generale, (int, float)) else "N/A"

    return tableau_dataframe


 

'''
# Tests
print("\n=== Tests ===")
# Ajouter un étudiant
print("\nAjout d'un étudiant :")
Ajout_Etudiant()
print("Tableau des étudiants après ajout :")
print(tableau_dataframe)

# Supprimer un étudiant
print("\nSuppression d'un étudiant :")
Supprimer_Etudiant()
print("Tableau des étudiants après suppression :")
print(tableau_dataframe)

# Rechercher un étudiant
print("\nRecherche d'un étudiant :")
Rechercher_Etudiant()


# Ajouter des notes
print("\nAjout de notes pour un étudiant :")
matricule_test = int(input("Entrez le matricule de l'étudiant pour ajouter des notes : "))
Recuperer_Notes(matricule_test)

# Calculer la moyenne
print("\nCalcul de la moyenne :")
matricule_test = int(input("Entrez le matricule de l'étudiant pour calculer la moyenne : "))
Calculer_moyenne(matricule_test)

# Classement des étudiants
print("\n--- Classement des étudiants par moyenne ---")
Classement_Etudiants()

# Notification des étudiants sous le seuil
print("\n--- Notification des étudiants en dessous du seuil ---")
seuil_test = int(input("Entrez le seuil de moyenne : "))
Notifier_Etudiants(seuil_test)

# Gestion des absences
print("\n--- Ajout et affichage des absences ---")
for matricule in tableau_dataframe['Matricule']:
    matiere_test = input(f"Entrez une matière pour ajouter une absence pour l'étudiant {matricule} : ")
    Ajouter_Absence(matricule, matiere_test)

print("\nAffichage des absences :")
for matricule in tableau_dataframe['Matricule']:
    Afficher_Absences(matricule)

# Générer les bulletins sous forme de tableau
print("\n--- Génération du bulletin des étudiants ---")
df_bulletin = Generer_Bulletin_DataFrame()
print("Bulletin des étudiants :")
print(df_bulletin)

# Supprimer un étudiant
print("\n--- Suppression d'un étudiant ---")
Supprimer_Etudiant()
print("Tableau des étudiants après suppression :")
print(tableau_dataframe)

# Rechercher un étudiant
print("\n--- Recherche d'un étudiant ---")
Rechercher_Etudiant()

# Authentification
print("\n--- Authentification d'un étudiant ---")
nom_test = input("Entrez le nom d'un étudiant pour vérifier son authentification : ")
matricule_test = input("Entrez le matricule de l'étudiant : ")
auth_result = Authentification(nom_test , matricule_test)
print(f"Résultat de l'authentification pour {nom_test} de matricule {matricule_test}:", "Validé" if auth_result else "Non trouvé")

print("\n=== Fin des tests ===")

'''



