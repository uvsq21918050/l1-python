import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk ## Importation des modules utiles dans PIL
from random import *
######################################################################################################################################
root = tk.Tk()

liste_couleur = ["blue","green","yellow","red","black"]
canvas = tk.Canvas(bg = "black", width = 600, height = 600)

#Initialisation des points pour la création des cercles
x0=0
y0=0
x1=600
y1=600

i = 0
while (x0 < (600/2) - 30 ):
    canvas.create_oval(x0,y0,x1,y1, fill=liste_couleur[i % 5])
    x0 += 10
    y0 += 10
    x1 -= 10
    y1 -= 10
    i += 1

canvas.pack()

######################################################################################################################################
# Fin de votre code
root.mainloop()