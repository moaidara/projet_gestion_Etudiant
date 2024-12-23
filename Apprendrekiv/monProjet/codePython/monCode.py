import pandas as pd
import os
import csv

#creation d'un objet etudiant avec ses propriete 
class Etudiant:
    def __init__(self, nom, prenom, nom_users, matricule, age, adresse, niveau, sex, numero, mail):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.adresse = adresse
        self.niveau = niveau
        self.nom_users = nom_users
        self.matricule = matricule
        self.sex = sex
        self.numero = numero
        self.mail = mail
    
    
    


#creation d'une fonction pour calculer la moyenne d'un etudiant
def calcul_Moyenne(NoteExamen, NoteDevoir):
        return (NoteExamen*0.6)+(NoteDevoir*0.4)

# recherche le matricule d'un etudiant dans le fichier etudiant.csv retourne False si: non trouver
def Rechercher_Matricule(matricule):
    dataFrame = Importation()
    dataFrame = dataFrame.astype({'Matricule': 'int64'})
    tableau_Mat = dataFrame.values.tolist()
    for mat in tableau_Mat:
        if mat[3]==matricule:
            return mat[3]
    return False
    
# cette fonction permet d'ajouter des notes a un etudiant via son matricule    
def Ajout_Note(Note_ExamenAN, Note_DevoirAN, matricule,Note_ExamenAL, Note_DevoirAL, Note_ExamenPR, Note_DevoirPR, Note_ExamenRE, Note_DevoirRE, Note_ExamenJA, Note_DevoirJA):
    dataFrame = Importation()
    dataFrame.columns = ['Nom', 'Prenom', 'Nom_users', 'Matricule', 'Age', 'Adresse', 'Niveau', 'Sex', 'Numero', 'Mail']
    #reconvertie les donnees nmerique du dataframe qui seront transformer en float a la recuperation
    dataFrame = dataFrame.astype({'Matricule': 'int64'})
    #creation d'un tableau pour recuperer les donnees du dataFrame
    tableau_Etudiant = dataFrame.values.tolist()
    # Rechercher l'étudiant dans le tableau
    etudiant = next((et for et in tableau_Etudiant if et[3] == matricule), None)
    Error = 'Error'
    Verifier=Rechercher_Matricule(matricule)
    
    #retourne false si le matricule n'est pas bonne
    if Verifier == False:
        return Error
    
    # si l'etudiant est trouver il lui ajoute les notes
    if etudiant:
        dataNoteAnglais = Importation_Note('Anglais')
        dataNoteAnglais.columns = ['Matricule', 'Note_Examen', 'Note_Devoir', 'Moyenne']
        new_noteAN={
            "Matricule": matricule,
            "Note_Examen":Note_ExamenAN, 
            "Note_Devoir": Note_DevoirAN,
            "Moyenne": calcul_Moyenne(Note_ExamenAN, Note_DevoirAN)
        }
        dataNoteAnglais = pd.concat([dataNoteAnglais, pd.DataFrame([new_noteAN])], ignore_index=True)
        Save_Note(dataNoteAnglais,'Anglais')


        dataNoteAlgo = Importation_Note('Algo')
        dataNoteAlgo.columns = ['Matricule', 'Note_Examen', 'Note_Devoir', 'Moyenne']
        new_noteAL={
            "Matricule": matricule,
            "Note_Examen":Note_ExamenAL, 
            "Note_Devoir": Note_DevoirAL,
            "Moyenne": calcul_Moyenne(Note_ExamenAL, Note_DevoirAL)
        }
        dataNoteAlgo = pd.concat([dataNoteAlgo, pd.DataFrame([new_noteAL])], ignore_index=True)
        Save_Note(dataNoteAlgo,'Algo')


        dataNoteProba = Importation_Note('Probabilite')
        dataNoteProba.columns = ['Matricule', 'Note_Examen', 'Note_Devoir', 'Moyenne']
        new_notePR={
            "Matricule": matricule,
            "Note_Examen":Note_ExamenPR, 
            "Note_Devoir": Note_DevoirPR,
            "Moyenne": calcul_Moyenne(Note_ExamenPR, Note_DevoirPR)
        }
        dataNoteProba = pd.concat([dataNoteProba, pd.DataFrame([new_notePR])], ignore_index=True)
        Save_Note(dataNoteProba,'Probabilite')


        dataNoteReseau = Importation_Note('Reseau')
        dataNoteReseau.columns = ['Matricule', 'Note_Examen', 'Note_Devoir', 'Moyenne']
        new_noteRE={
            "Matricule": matricule,
            "Note_Examen":Note_ExamenRE, 
            "Note_Devoir": Note_DevoirRE,
            "Moyenne": calcul_Moyenne(Note_ExamenRE, Note_DevoirRE)
        }
        dataNoteReseau = pd.concat([dataNoteReseau, pd.DataFrame([new_noteRE])], ignore_index=True)
        Save_Note(dataNoteReseau,'Reseau')


        dataNoteJava = Importation_Note('Java')
        dataNoteJava.columns = ['Matricule', 'Note_Examen', 'Note_Devoir', 'Moyenne']
        new_noteJA={
            "Matricule": matricule,
            "Note_Examen":Note_ExamenJA, 
            "Note_Devoir": Note_DevoirJA,
            "Moyenne": calcul_Moyenne(Note_ExamenJA, Note_DevoirJA)
        }
        dataNoteJava = pd.concat([dataNoteJava, pd.DataFrame([new_noteJA])], ignore_index=True)
        Save_Note(dataNoteJava,'Java')
        return True
    else:
        return False

#la fonction afficher note qui retourne les notes d'un etudiant en prenant commme parametre le matiere et le matricule de l'etudiant
def Afficher_Note(matiere, matricule):
    dataFrame = Importation_Note(matiere)
    # dataFrame = dataFrame.astype({'Matricule':'int64', 'Note_Examen':'int64', 'Note_Devoir':'int'})
    tableauNote = dataFrame.values.tolist()
    etudiant = next((et for et in tableauNote if et[0] == matricule), None)
    if etudiant:
       Note_Examen = int(etudiant[1])
       Note_Devoir = int(etudiant[2])
       Moyenne=etudiant[3]
       return Note_Examen, Note_Devoir, Moyenne
    else: 
       #retourne false si non trouver
       return False
    

#la fonction pour modifier les notes d'un etudiant
#prend en parametre la matiere a modifier le matricule et les nouveau notes
def Modifier_Note(matiere, matricule, Note_Examen, Note_Devoir):
    dataFrame = Importation_Note(matiere)
    dataFrame= dataFrame.astype(int)
    print(dataFrame)
    tableauNote = dataFrame.values.tolist()
    for note in tableauNote:
        if note[0]==matricule:
            note[1] = Note_Examen
            note[2] = Note_Devoir
            note[3] = calcul_Moyenne(Note_Examen, Note_Devoir)
            dataFrame = pd.DataFrame(tableauNote, columns=['Matricule', 'Note_Examen', 'Note_Devoir', 'Moyenne'])
            #Enregistrement des donnees modifier dans le fichier etudiant.csv
            Save_Note(dataFrame, matiere)
            return True
    return False 


#cette fonction permet l'importation des donnes du fichier sur lequels est stocker les note sur une matiere
#elle renvoie ces donnees sous forme de DataFrame
def Importation_Note(matiere):
    match matiere:
        case 'Anglais':
            chemin_Note= 'C:/Users/DELL/Desktop/projet_gestion_Etudiant/Apprendrekiv/monProjet/maBase/anglais.csv'
        case 'Probabilite':
            chemin_Note= 'C:/Users/DELL/Desktop/projet_gestion_Etudiant/Apprendrekiv/monProjet/maBase/probabilite.csv'
        case 'Reseau':
            chemin_Note= 'C:/Users/DELL/Desktop/projet_gestion_Etudiant/Apprendrekiv/monProjet/maBase/reseau.csv'
        case 'Java':
            chemin_Note= 'C:/Users/DELL/Desktop/projet_gestion_Etudiant/Apprendrekiv/monProjet/maBase/java.csv'
        case 'Algo':
            chemin_Note= 'C:/Users/DELL/Desktop/projet_gestion_Etudiant/Apprendrekiv/monProjet/maBase/algo.csv'
        case 'Bultin':
            chemin_Note= 'C:/Users/DELL/Desktop/projet_gestion_Etudiant/Apprendrekiv/monProjet/maBase/bultin.csv'

    if not os.path.exists(chemin_Note) or os.stat(chemin_Note).st_size ==0:
        pd.DataFrame(columns=['Matricule', 'Note_Examen', 'Note_Devoir', 'Moyenne']).to_csv(chemin_Note, index=False)
    return pd.read_csv(chemin_Note)

#cette fonction d'enregister les donner d'un dataFrame sur un un fichier 
# elle prend en entrer le dataFrame et la matiere qui pourras specifier le fichier sur lequel on doit stocker ces donnees    
def Save_Note(dataNote,matiere):
    match matiere:
        case 'Anglais':
            chemin_Note= 'C:/Users/DELL/Desktop/projet_gestion_Etudiant/Apprendrekiv/monProjet/maBase/anglais.csv'
        case 'Probabilite':
            chemin_Note= 'C:/Users/DELL/Desktop/projet_gestion_Etudiant/Apprendrekiv/monProjet/maBase/probabilite.csv'
        case 'Reseau':
            chemin_Note= 'C:/Users/DELL/Desktop/projet_gestion_Etudiant/Apprendrekiv/monProjet/maBase/reseau.csv'
        case 'Java':
            chemin_Note= 'C:/Users/DELL/Desktop/projet_gestion_Etudiant/Apprendrekiv/monProjet/maBase/java.csv'
        case 'Algo':
            chemin_Note= 'C:/Users/DELL/Desktop/projet_gestion_Etudiant/Apprendrekiv/monProjet/maBase/algo.csv'
        case 'Bultin':
            chemin_Note= 'C:/Users/DELL/Desktop/projet_gestion_Etudiant/Apprendrekiv/monProjet/maBase/bultin.csv'

    dataNote.to_csv(chemin_Note, index=False)


#creation d'un objet admin avec ces proprietes
class Admin:
    def __init__(self, nom_admin, matricule_admin):
        self.nom_admin = nom_admin
        self.matricule_admin = matricule_admin

# creation de deux instance de la class admin
admin1=Admin('aidara300', 123456)       
admin2=Admin('laye300', 123456) 
admin_tab=[[admin1.nom_admin,admin1.matricule_admin],[admin2.nom_admin,admin2.matricule_admin]]

#cette fonction verifie l'authentification des admin pour l'interface de connexion
def Authentification(nomUsers, matricule):
    global admin_tab
    for admin in admin_tab:
        if (admin[0]== nomUsers) & (admin[1] == matricule):
            return True
    else:
        return False
    
# Fonction pour ajouter un nouvel étudiant dans la base de données
def Ajout_Etudiant(nom,prenom,nom_users,matricule:int,age:int,adresse,niveau,sex,numero:int, mail):
    Error = 'Error'
    Verifier=Rechercher_Matricule(matricule)   
    # Vérifie si un étudiant avec le même matricule existe déj
    if Verifier != False:
        return Error
    
    # Importation des données actuelles des étudiants
    dataframe = Importation()
    dataframe.columns = ['Nom', 'Prenom', 'Nom_users', 'Matricule', 'Age', 'Adresse', 'Niveau', 'Sex', 'Numero', 'Mail']
    # Création d'un nouvel étudiant sous forme d'objet
    etudiant = Etudiant(nom,prenom,nom_users,matricule,age,adresse,niveau,sex,numero, mail)
    # Prépare les données pour ajouter le nouvel étudiant
    new_data={
        'Nom':etudiant.nom,
        'Prenom':etudiant.prenom,
        'Nom_users':etudiant.nom_users,
        'Matricule':int(etudiant.matricule),
        'Age':int(etudiant.age),
        'Adresse':etudiant.adresse,
        'Niveau':etudiant.niveau,
        'Sex':etudiant.sex,
        'Numero':int(etudiant.numero),
        'Mail':etudiant.mail
    }
    # Ajoute le nouvel étudiant aux données existantes
    tableau_DataFrame = pd.concat([dataframe, pd.DataFrame([new_data])], ignore_index=True)
    print(tableau_DataFrame)
    MisAJour(tableau_DataFrame)
    return True

# Fonction pour importer les données des étudiants depuis un fichier CSV
def Importation():
    etudiantCsv = 'C:/Users/DELL/Desktop/projet_gestion_Etudiant/Apprendrekiv/monProjet/maBase/etudiant.csv'
    # Vérifie si le fichier existe ou est vide, et le crée si nécessaire
    if not os.path.exists(etudiantCsv) or os.stat(etudiantCsv).st_size == 0:
        # Créer un fichier vide avec les colonnes nécessaires
        pd.DataFrame(columns=['Nom', 'Prenom', 'Nom_users', 'Matricule', 'Age', 
                              'Adresse', 'Niveau', 'Sex', 'Numero', 'Mail']).to_csv(etudiantCsv, index=False)
    return pd.read_csv(etudiantCsv)

# Fonction pour mettre à jour les données des étudiants dans le fichier CSV    
def MisAJour(tdataFrame):
    etudiantCsv = 'C:/Users/DELL/Desktop/projet_gestion_Etudiant/Apprendrekiv/monProjet/maBase/etudiant.csv'
    tdataFrame.to_csv(etudiantCsv, index=False)

# Ajout_Etudiant('Mansour', 'Aidara', 'aidara300', 1234565, 21, 'Medina', 'l2', 'M', 774789900, '@mail')

# Fonction pour supprimer un étudiant en utilisant son matricule
def Supprimer_Etudiant(matricule):
    dataframe = Importation()
    tableau_Etudiant = dataframe.values.tolist()
    # Trouver l'index de l'étudiant dans le tableau(son matricule)
    index_a_supprimer = next((index for index, etudiant in enumerate(tableau_Etudiant) if etudiant[3] == matricule), False)
    if index_a_supprimer is not False:
        tableau_Etudiant.pop(index_a_supprimer)
        dataframe= pd.DataFrame(tableau_Etudiant, columns=['Nom', 'Prenom', 'Nom_users', 'Matricule', 'Age', 'Adresse', 'Niveau', 'Sex', 'Numero', 'Mail'])
        print(dataframe)
        MisAJour(dataframe)
        return True
    else:
        return False
    

# Fonction pour rechercher un étudiant en utilisant son matricule
def Rechercher_Etudiant(matricule):
    dataframe = Importation()
    tableau_Etudiant = dataframe.values.tolist()
    # Rechercher l'étudiant dans le tableau
    etudiant = next((et for et in tableau_Etudiant if et[3] == matricule), None)
    if etudiant:
        nom = etudiant[0]
        prenom = etudiant[1]
        age = etudiant[2]
        adresse = etudiant[4]
        niveau = etudiant[5]
        nom_users = etudiant[6]
        sex = etudiant[7]
        numero = etudiant[8]
        mail = etudiant[9] 
        return nom, prenom, age, adresse, nom_users, numero, mail, niveau, sex
    else:
        return False


# Fonction pour modifier les informations d'un étudiant existant
def ModifierEtudiant(nom,prenom,nom_users,matricul,age,adresse,niveau,sex,numero, mail):

    dataframe = Importation()
    print(dataframe)
    tableau_Etudiant = dataframe.values.tolist() 
    # Parcourt la liste pour trouver l'étudiant à modifier
    for etudiant in tableau_Etudiant:
        if etudiant[3] == matricul :
            etudiant[0] = nom
            etudiant[1] = prenom
            etudiant[2] = nom_users
            etudiant[3] = matricul
            etudiant[4] = age
            etudiant[5] = adresse
            etudiant[6] = niveau
            etudiant[7] = sex
            etudiant[8] = numero
            etudiant[9] = mail
            dataframe= pd.DataFrame(tableau_Etudiant, columns=['Nom', 'Prenom', 'Nom_users', 'Matricule', 'Age', 'Adresse', 'Niveau', 'Sex', 'Numero', 'Mail'])
            print(dataframe)
            MisAJour(dataframe)
            return True
    return False

# Fonction pour générer un bulletin de notes pour un étudiant
def Generer_Bultin(matricule):
    fichier_Name = 'C:/Users/DELL/Desktop/projet_gestion_Etudiant/Apprendrekiv/monProjet/maBase/bultin.csv'

    # Réinitialise le fichier de bulletin
    with open(fichier_Name, mode='r', newline='', encoding='utf-8') as fichier:
            reader = csv.reader(fichier)
            premiere_ligne = next(reader, None)  # Récupère la première ligne
        

        
        # Réécrire le fichier avec uniquement la première ligne
    with open(fichier_Name, mode='w', newline='', encoding='utf-8') as fichier:
        writer = csv.writer(fichier)
        writer.writerow(premiere_ligne)

    # Récupère les notes pour chaque matière
    NoteAN = Afficher_Note('Anglais', matricule)
    Note_ExamenAN = NoteAN[0]
    Note_DevoirAN = NoteAN[1]
    MoyenneAN = NoteAN[2]
    
    NoteAL = Afficher_Note('Algo', matricule)
    Note_ExamenAL = NoteAL[0]
    Note_DevoirAL = NoteAL[1]
    MoyenneAL = NoteAL[2]

    NoteJA = Afficher_Note('Java', matricule)
    Note_ExamenJA = NoteJA[0]
    Note_DevoirJA = NoteJA[1]
    MoyenneJA = NoteJA[2]

    NotePR = Afficher_Note('Probabilite', matricule)
    Note_ExamenPR = NotePR[0]
    Note_DevoirPR = NotePR[1]
    MoyennePR = NotePR[2]

    NoteRE = Afficher_Note('Reseau', matricule)
    Note_ExamenRE = NoteRE[0]
    Note_DevoirRE = NoteRE[1]
    MoyenneRE = NoteRE[2]
    
    MoyenneGN = (MoyenneAL + MoyenneAN + MoyenneRE + MoyenneJA + MoyennePR)/5
    # Prépare les données du bulletin
    Tableau_Bultin = [['Anglais', Note_ExamenAN, Note_DevoirAN, MoyenneAN],
                      ['Algo', Note_ExamenAL, Note_DevoirAL, MoyenneAL],
                      ['Java', Note_ExamenJA, Note_DevoirJA, MoyenneJA],
                      ['Probabilite', Note_ExamenPR, Note_DevoirPR, MoyennePR],
                      ['Reseau', Note_ExamenRE, Note_DevoirRE, MoyenneRE],
                      ['Moyenne generale', '', '', MoyenneGN]]
    # Sauvegarde le bulletin sous forme de DataFrame
    data_Bultin = pd.DataFrame(Tableau_Bultin, columns=['Matiere', 'Note_Examen', 'Note_Devoir', 'Moyenne'])
    Save_Note(data_Bultin, 'Bultin')

# Generer_Bultin(1234823)




# ModifierEtudiant('Mouhamed','Aidara','aidara300',1234565,21,'Medina','Licence2','Masculin',774789900,'@mail')   

# Ajout_Note(2,4,1234565)   
# Ajout_Note(12, 13,123489,13, 14,14, 11, 15, 10, 19, 20)

# print(Afficher_Note('Anglais',1234565))

# Modifier_Note('Algo', 1234565, 10, 12)

# print(Generer_Bultin(1234565))

