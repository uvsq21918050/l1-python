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

#Variable de contrôle pour le compteur
val_compteur = tk.StringVar()
val_compteur.set("0")



liste_couleur = ["blue","green","yellow","red", "white"]

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
    a = randint(0,4)
    if ( C.coords(identifiant_cercle)[2] < 600 ):
        C.move(identifiant_cercle, dep,0)
    else :
        #Mise à jour du compteur
        val = int(val_compteur.get())
        val += 1
        val_compteur.set(str(val))
        global identifiant_compteur
        C.itemconfig(identifiant_compteur, text =  "Compteur : " + val_compteur.get())

        C.delete(identifiant_cercle)
        identifiant_cercle = C.create_oval(x1,y1,x2,y2, fill = liste_couleur[a])
    pass

def recule_cercle():
    global identifiant_cercle
    if ( C.coords(identifiant_cercle)[0] >= (0 + dep) ):
        C.move(identifiant_cercle, -dep,0)
    else : print("Ne recule pas")
    pass

def reset():
    global identifiant_cercle
    C.delete(identifiant_cercle)
    identifiant_cercle = C.create_oval(x1,y1,x2,y2, fill = liste_couleur[0])
    
    global identifiant_compteur
    val_compteur.set("0")
    C.itemconfig(identifiant_compteur, text =  "Compteur : " + val_compteur.get())
    pass



##################################
C = tk.Canvas(background = "black", width = CANVAS_WIDTH, height = CANVAS_HEIGHT)
B_A = tk.Button(text = "AVANCER", command = lambda :avance_cercle(liste_couleur))
B_R = tk.Button(text = "RECULER", command = recule_cercle)
B_Reset = tk.Button(text = "RESET", command = reset)
identifiant_compteur = C.create_text(550, 25, text = "Compteur : " + val_compteur.get()  , fill = "white")


#POSITIONNEMENT DES OBJETS
B_A.grid(row = 0, column = 1)
B_R.grid(row = 0, column = 2)
B_Reset.grid(row = 0, column = 3)
C.grid(row = 1, column = 0, columnspan = 4)




###############CODE FONCTIONNEMENT###############
C.bind("<Button-1>", initialize_cercle) 









###################################
fenetre.mainloop()
