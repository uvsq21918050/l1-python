

def afficheCarre(carre):
    for i in range(0, len(carre)):
        for j in range(0, len(carre[i])):
            print(carre[i][j], end= " ") #Affiche l'element à la i eme ligne et a la j eme colonne
        print("\n")
    pass


def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si toutes les lignes ont la même somme, et -1 sinon """
    liste_somme_ligne = [0,0,0,0]
    for i in range(0, len(carre)):
        for j in range(0, len(carre[i])):
            liste_somme_ligne[i] += carre[i][j]   

    #Verifier que les elements de ma liste sont égaux.
    val = liste_somme_ligne[0]
    for i in range(1, len(liste_somme_ligne)):
        if (val != liste_somme_ligne[i]):
            return -1
    return val

def testColonnesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si toutes les lignes ont la même somme, et -1 sinon """
    liste_somme_colonne = [0,0,0,0]
    for i in range(0, len(carre)):
        for j in range(0, len(carre[i])):
            liste_somme_colonne[i] += carre[j][i]   

    #Verifier que les elements de ma liste sont égaux.
    val = liste_somme_colonne[0]
    for i in range(1, len(liste_somme_colonne)):
        if (val != liste_somme_colonne[i]):
            return -1
    return val

def testDiagonalesEgales(carre):
    """ Renvoie la somme des éléments d'une diagonale de la liste 2D carre si les 2 diagonales ont la même somme, et -1 sinon """
    somme_diag_1 = 0
    somme_diag_2 = 0
    
    for i in range(0, len(carre)):
        for j in range(0, len(carre[i])): 
            if(i == j):
                somme_diag_1 += carre[i][j]
                somme_diag_2 += carre[i][3 - j]
    
    if(somme_diag_1 != somme_diag_2):
        return -1
    
    return somme_diag_1

def estCarreMagique(carre):
    """ Renvoie True si c'est un carre magique et False sinon"""
    if (testLignesEgales(carre) == -1 or testColonnesEgales(carre) == -1 or testDiagonalesEgales(carre) == -1):
        return False
    
    return True


#####################################################################

carre_mag = [ [4,14,15,1], [9,7,6,12], [5,11,10,8], [16,2,3,13]] 
carre_pas_mag = [ [4,14,15,1], [9,7,6,12], [5,11,10,8], [16,2,7,13] ]

print(estCarreMagique(carre_mag))
print(estCarreMagique(carre_pas_mag))


