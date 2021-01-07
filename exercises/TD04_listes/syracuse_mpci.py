from random import *

##################### ZONE DE DEFINITION DES FONCTIONS #########################

def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    liste_valeurs_successives = [ ]
    while (n != 1):
        if (n % 2 == 0):
            n = n // 2 
        else:
            n = n * 3 + 1
        liste_valeurs_successives.append(n)
    return liste_valeurs_successives

def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """
    a = []
    for i in range(2, n_max):
        a = syracuse(i)
        if (a[-1] == 1):
            print("Pour n = ", i, "Syracuse est TRUE")
        
    pass

def tempsVol(n):
    """ Retourne le temps de vol de n """
    #1- Calculer syracuse pour la valeur de n en paramètre et récupérer la liste des valeurs
    liste_valeurs_n = syracuse(n)
    #2- La liste des valeurs contient toutes les valeurs de n jusqu'à 1
    #DONC si on récupère la taille de cette liste ALORS on récupère le nombres d'étapes qui nous ont permis d'aller de n à 1
    nombre_valeurs = len( liste_valeurs_n )
    return nombre_valeurs

def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    print(n_max)
    a = [ ] #A contiendra tous les temps de vol
    for n in range(1, n_max + 1):
        a.append(tempsVol(n))  # n sera entre 1 et nmax. La fonction tempsVol renvoie un nombre
    return a

def temps_volMAX(n_max):
    a = tempsVolListe(n_max) #a contiendra tous les temps de vol de 1 a nmax
    #Il faut parcourir tous les elements de ma liste
    temps_vol_max = 0
    indice_n = 0
    for i in range(0, n_max):
        if (temps_vol_max < a[i] ):
            temps_vol_max = a[i]
            indice_n = i+1

    return (indice_n, temps_vol_max)        

def altitude_maximale_n(n):
    a = [ ]
    a = syracuse(n)
    a.sort()
    return a[-1]

def liste_altitude_maximales(n_max):
    a = [ ]
    for n in range(2, n_max + 1):
        a.append( altitude_maximale_n(n) )
    return a

def altitude_max_liste_altitudes_max(liste):
    alti_max = 0
    indice_alti_max = 0
    for n in range(0, len(liste)):
        if( alti_max < liste[n]):
            alti_max = liste[n]
            indice_alti_max = n+2
    return (indice_alti_max, alti_max)


##################################################################################
n_max = 10000

#clear
a = liste_altitude_maximales(n_max)
print( altitude_max_liste_altitudes_max(a))
liste_une_dimension = [ 1,2,3 ] #A ligne et trois colonnes
liste_deux_dimensions = [ [1,2,3], [4,5,6], [7,8,9]  ]
print(liste_deux_dimensions[2])

