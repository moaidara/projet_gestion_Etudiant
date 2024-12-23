from kivy.uix.screenmanager import ScreenManager
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
import pandas as pd
import acceuil
from codePython import monCode


# Classe pour gérer les écrans et les actions dans l'application

class MonGestionnaireEcran(ScreenManager):
    # variable pour stocker les informations de l'étudiant
    nomSS=''
    prenomSS = ''
    ageSS = ''
    adresseSS = ''
    nom_usersSS = ''
    niveauSS = ''
    sexSS = ''
    mailSS = ''
    numeroSS = ''
    message= StringProperty("")
    # Vérifie les informations de connexion de l'utilisateur
    def check_Authentification(self, loginPC:str, mdpdPC:int):
        try:
            mdpdPC= int(mdpdPC)
            result=monCode.Authentification(loginPC,mdpdPC)
            if(result==True):
                self.current="acceuil"
        except ValueError:
            print("Erreur")
        
    # Ajoute un nouvel étudiant dans le système    
    def add_student(self, nomAJ:str, prenomAJ:str, nom_usersAJ:str, matriculeAJ:int, ageAJ:int, adresseAJ:str, niveauAJ:str, sexAJ:str, numeroAJ:int, mailAJ:str ):
        try:
            # Conversion des champs numériques en entiers
            matriculeAJ=int(matriculeAJ)
            numeroAJ=int(numeroAJ)
            ageAJ=int(ageAJ)
             # Ajoute l'étudiant via une fonction externe
            result=monCode.Ajout_Etudiant(nomAJ, prenomAJ, nom_usersAJ, matriculeAJ, ageAJ, adresseAJ, niveauAJ, sexAJ, numeroAJ, mailAJ)
            print(result)
            if(result==True):
                self.message='Etudiant Ajoute Avec Succes'
            elif(result=='Error'):
                self.message='le matricule entre existe deja'
        except:
            self.message="les champs matricule, age et numero sont des nombres!"
        
            
   # Supprime un étudiant en fonction de son matricule
    def remove_Student(self, matricule:int):
        try:
            matricule=int(matricule)
            result=monCode.Supprimer_Etudiant(matricule)
            print(result)
            if result:
                self.message="etudiant suprimer"
            else:
                self.message="le matricule non valide"
        except:
            self.message='verifier que les champs sont bien remplie!'
    
    # Modifie les informations d'un étudiant
    def Modify_Student(self, nom,prenom,nom_users,matricul,age,adresse,niveau,sex,numero, mail):
        try:
            self.age=int(age)
            self.numero=int(numero)
            matricul=int(matricul)
            result=monCode.ModifierEtudiant(nom,prenom,nom_users,matricul,age,adresse,niveau,sex,numero, mail)
            self.message = "Modification reussie"
            print(result)
        except:
            self.message='les champs matricule, age et numero sont des nombres!'

    # Recherche un étudiant en fonction de son matricule
    def Search_Student(self, matricule:int):
        try:
            matricule = int(matricule)
            resultSS=monCode.Rechercher_Etudiant(matricule)
            if resultSS != False:
                print(resultSS)
                self.nomSS = resultSS[0]
                self.prenomSS = resultSS[1]
                self.nom_usersSS = resultSS[2]
                self.ageSS = resultSS[3]
                self.niveauSS=resultSS[4]
                self.numeroSS = resultSS[5]
                self.mailSS = resultSS[6]
                self.adresseSS=resultSS[7] 
                self.sexSS = resultSS[8]
            else :
                self.message='le matricule entrer n\'est pas valide'
        except:
            self.message='verifier que les champs sont bien remplie!'

    # Génère un bulletin pour un étudiant donné
    def Search_StudentBultin(self, matricule):
        try:
            matricule = int(matricule)
            result = monCode.Rechercher_Matricule(matricule)
            print(result)
            if result != False:
                monCode.Generer_Bultin(matricule)
                self.current = 'AfficherBultin'  
            else:
                self.message='le matricule entrer n\'est pas valide'
        except:
            self.message='le champs matricule est un nombre!'

    # Ajout des notes pour un étudiant
    def Add_Note(self,Note_ExamenAN, Note_DevoirAN, matricule,Note_ExamenAL, Note_DevoirAL, Note_ExamenPR, Note_DevoirPR, Note_ExamenRE, Note_DevoirRE, Note_ExamenJA, Note_DevoirJA):
        try:
            matricule = int(matricule)
            Note_ExamenAN = int(Note_ExamenAN)
            Note_DevoirAN = int(Note_DevoirAN)
            Note_ExamenAL = int(Note_ExamenAL)
            Note_DevoirAL = int(Note_DevoirAL)
            Note_ExamenPR = int(Note_ExamenPR)
            Note_DevoirPR = int(Note_DevoirPR)
            Note_ExamenRE = int(Note_ExamenRE)
            Note_DevoirRE = int(Note_DevoirRE)
            Note_ExamenJA = int(Note_ExamenJA)
            Note_DevoirJA = int(Note_DevoirJA)
            result = monCode.Ajout_Note(Note_ExamenAN, Note_DevoirAN, matricule,Note_ExamenAL, Note_DevoirAL, Note_ExamenPR, Note_DevoirPR, Note_ExamenRE, Note_DevoirRE, Note_ExamenJA, Note_DevoirJA)
            print(result)
            if result == True:
                self.message='les notes sont bien ajoute'
            elif result == 'Error':
                self.message='matricule non valide'
                print(result)
        except:
            self.message="verifier si les champs sont bien remplis"

    # Modifie les notes d'une matière pour un étudiant
    def Change_Note(self,matiere, matricule, Note_Examen, Note_Devoir):
        try:
            matricule = int(matricule)
            Note_Examen = int(Note_Examen)
            Note_Devoir = int(Note_Devoir)
            result = monCode.Modifier_Note(matiere, matricule, Note_Examen, Note_Devoir)
            if result:
                self.message='notes bien modifie'
            else:
                self.message='matricule non valide'
        except:
            self.message="verifier si les champs sont bien remplis"

    pass