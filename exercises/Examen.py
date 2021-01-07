import tkinter as tk
from random import *
fenetre = tk.Tk()      #Création de la fenetre graphique "root"

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600

#Variable globale 
identifiant_cercle = 0
compteur = 0

#Points pour construire le cercle (x1,y1) et (x2,y2)
x1 = 0
y1 = 250

x2 = 100
y2 = 350 

liste_couleur = ["blue","green","yellow","red","black", "white"]

def initialize_cercle(event):
    global identifiant_cercle
    global compteur
    
    if (compteur < 1):
        identifiant_cercle = C.create_oval(x1,y1,x2,y2, fill = "blue")
        print("L'identifiant est :", identifiant_cercle)
        compteur += 1
    else : print("On ne crée pas de nouveau cercle")
    pass

#fonction appelée lors d'un clic sur le bouton "avancer"
dep = 100

def avance_cercle(liste_couleur):
    global identifiant_cercle
    a = randint(0,5)
    if ( C.coords(identifiant_cercle)[2] < 600 ):
        C.move(identifiant_cercle, dep,0)
    else :
        C.delete(identifiant_cercle)
        identifiant_cercle = C.create_oval(x1,y1,x2,y2, fill = liste_couleur[a])
    pass

def recule_cercle():
    global identifiant_cercle
    if ( C.coords(identifiant_cercle)[0] >= (0 + dep) ):
        C.move(identifiant_cercle, -dep,0)
    else : print("Ne recule pas")
    pass

#.move(identifiant_objet, dep_x, dep_y)

##################################
C = tk.Canvas(background = "black", width = CANVAS_WIDTH, height = CANVAS_HEIGHT)
B_A = tk.Button(text = "AVANCER", command = lambda :avance_cercle(liste_couleur))
B_R = tk.Button(text = "RECULER", command = recule_cercle)


#POSITIONNEMENT DES OBJETS
B_A.grid(row = 0, column = 1)
B_R.grid(row = 0, column = 2)
C.grid(row = 1, column = 0, columnspan = 4)




###############CODE FONCTIONNEMENT###############
C.bind("<Button-1>", initialize_cercle) 









###################################
fenetre.mainloop()
