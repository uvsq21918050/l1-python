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


###################### ZONE DE PROGRAMME PRINCIPAL ##############################

n_max = randint(10000,100000)
print(testeConjecture(n_max))