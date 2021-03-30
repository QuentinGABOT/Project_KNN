# -*- coding: utf-8 -*-
"""
Created on Fri May 22 23:22:13 2020

@author: quent
"""

import numpy as np
import csv

liste_finale = []
liste_apprentissage = []

# CHARGEMENT DU DATASET

def Chargement(liste):
    with open(r'C:\Users\quent\Documents\S6\IA\KNN\data.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            ligne = ''.join(row)
            liste.append(ligne.split(';'))   
    del liste[-1] 
    
    
def ChargementFinal(liste):       
    with open(r'C:\Users\quent\Documents\S6\IA\KNN\finalTest.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            ligne = ''.join(row)
            liste.append(ligne.split(';'))   
    del liste[-1]
    
def Initialisation():
    Chargement(liste_apprentissage)
    ChargementFinal(liste_finale)
    print("La liste du dataset : ")
    print(liste_finale)
    print("\n")        
    print("La liste d'apprentissage : ")
    print(liste_apprentissage)
   
    
def MoyenneApprentissage(liste_apprentissage):
    mean_apprentissage = []
    for k in range(4):
        mean_apprentissage.append(np.mean([float(x[k]) for x in liste_apprentissage]))
    return mean_apprentissage

def MoyenneEvaluation(liste_finale):
    mean_evaluation = []
    for k in range(4):
        mean_evaluation.append(np.mean([float(x[k]) for x in liste_finale]))
    return mean_evaluation

def VarianceApprentissage(liste_apprentissage):
    var_apprentissage = []
    for k in range(4):
        var_apprentissage.append(np.std([float(x[k]) for x in liste_apprentissage]))
    return var_apprentissage

def VarianceEvaluation(liste_finale):
    var_evaluation = []
    for k in range(4):
        var_evaluation.append(np.std([float(x[k]) for x in liste_finale]))
    return var_evaluation


# CALCUL DE LA DISTANCE SEPARANT L'ELEMENT TIRE DE LA LISTE D'EVALUATION 
# PAR RAPPORT A UN ELEMENT DE LA LISTE D'APPRENTISSAGE

def Distance(i, j, liste_apprentissage, liste_finale,
              var_apprentissage, var_evaluation,
              mean_apprentissage, mean_evaluation):
   
    retour = 0
    for k in range(4):        
        retour += (((float(j[k]) - mean_apprentissage[k])/var_apprentissage[k]) - 
                    ((float(i[k]) - mean_evaluation[k])/var_evaluation[k]))**2
    return retour**0.5

# ON PROCEDE AU VOTE DE LA CLASSE VIA LES K-PLUS PROCHES VOISINS

def Vote(liste):
    compteur1 = 0
    compteur2 = 0
    compteur3 = 0
    compteur4 = 0
    compteur5 = 0
    compteur6 = 0
    compteur7 = 0
    compteur8 = 0
    compteur9 = 0
    compteur10 = 0
    retour = ''
    for x in liste:
        if (x[1] == 'A'):
            compteur1 += (10 - x[0])
        else:
            if (x[1] == 'B'):
                compteur2 += (10 - x[0])
            else:
                if (x[1] == 'C'):
                    compteur3 += (10 - x[0])
                else:
                    if (x[1] == 'D'):
                        compteur4 += (10 - x[0])  
                    else:
                        if (x[1] == 'E'):
                            compteur5 += (10 - x[0])
                        else:
                            if (x[1] == 'F'):
                                compteur6 += (10 - x[0])    
                            else:
                                if (x[1] == 'G'):
                                    compteur7 += (10 - x[0])
                                else:
                                    if (x[1] == 'H'):
                                        compteur8 += (10 - x[0])
                                    else:
                                        if (x[1] == 'I'):
                                            compteur9 += (10 - x[0])    
                                        else:
                                            if (x[1] == 'J'):
                                                compteur10 += (10 - x[0])                                    
                    
    if ((compteur1 > compteur2) and (compteur1 > compteur3) and (compteur1 > compteur4) 
        and (compteur1 > compteur5) and (compteur1 > compteur6) and (compteur1 > compteur7)
        and (compteur1 > compteur8) and (compteur1 > compteur9) and (compteur1 > compteur10)):
        retour = 'A'
    else:
        if ((compteur2 > compteur3) and (compteur2 > compteur4) and (compteur2 > compteur5) 
            and (compteur2 > compteur6) and (compteur2 > compteur7) and (compteur2 > compteur8) 
            and (compteur2 > compteur9) and (compteur2 > compteur10)):
            retour = 'B'
        else:
            if ((compteur3 > compteur4) and (compteur3 > compteur5) and (compteur3 > compteur6)
                and (compteur3 > compteur7) and (compteur3 > compteur8) 
                and (compteur3 > compteur9) and (compteur3 > compteur10)):
                retour = 'C'
            else:
                if ((compteur4 > compteur5) and (compteur4 > compteur6) 
                    and (compteur4 > compteur7) and (compteur4 > compteur8) 
                    and (compteur4 > compteur9) and (compteur4 > compteur10)):
                    retour = 'D'
                else:
                    if ((compteur5 > compteur6) and (compteur5 > compteur7) 
                        and (compteur5 > compteur8) and (compteur5 > compteur9) 
                        and (compteur5 > compteur10)):
                        retour = 'E'
                    else:
                        if ((compteur6 > compteur7) and (compteur6 > compteur8) 
                            and (compteur6 > compteur9) and (compteur6 > compteur10)):
                            retour = 'F'
                        else:
                            if ((compteur7 > compteur8) and (compteur7 > compteur9) 
                                and (compteur7 > compteur10)):
                                retour = 'G'
                            else:
                                if ((compteur8 > compteur9) and (compteur8 > compteur10)):
                                    retour = 'H'
                                else:
                                   if ((compteur9 > compteur10)):
                                       retour = 'I'
                                   else:
                                       retour = 'J'
    return retour    
    
def Test():
    liste = []
    var_apprentissage = VarianceApprentissage(liste_apprentissage)
    var_evaluation = VarianceEvaluation(liste_finale)
    mean_apprentissage = MoyenneApprentissage(liste_apprentissage)
    mean_evaluation = MoyenneEvaluation(liste_finale)
    retour = []
    for k in range(4, 5):        
        for i in liste_finale:
            for j in liste_apprentissage:
                nombre = Distance(i, j, liste_apprentissage, liste_finale,
                                  var_apprentissage, var_evaluation,
                                  mean_apprentissage, mean_evaluation)
                tup = (nombre, j[4])
                liste.append(tup)  
            liste.sort(key = lambda x:x[0])           
            liste = liste[0 : k]
            classe = Vote(liste)
            retour.append(classe)                                                                           
            liste[:] = []        
    return retour

def Ecriture(ecrit):
    file = open(r'C:\Users\quent\Documents\S6\IA\KNN\Gabot.txt','a') 
    for line in ecrit:        
        file.write(line)
        file.write("\n")
    file.close()
        
def main():
    Initialisation()
    Ecriture(Test())
    
if __name__=='__main__':    
    main()    


