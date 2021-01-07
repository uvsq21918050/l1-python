import tkinter as tk
fenetre = tk.Tk()      #Création de la fenetre graphique "root"

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600

##################################
C = tk.Canvas(background = "black", width = CANVAS_WIDTH, height = CANVAS_HEIGHT)
B_A = tk.Button(text = "AVANCER")
B_R = tk.Button(text = "RECULER")

#POSITIONNEMENT DES OBJETS
B_A.grid(row = 0, column = 1)
B_R.grid(row = 0, column = 2)
C.grid(row = 1, column = 0, columnspan = 4)

#Points pour construire le cercle (x1,y1) et (x2,y2)
x1 = 0
y1 = 250

x2 = 100
y2 = 350 

def initialize_cercle(event):
    C.create_oval(x1,y1,x2,y2, fill = "blue")
    pass

###############CODE FONCTIONNEMENT###############
C.bind("<Button-1>", initialize_cercle) 









###################################
fenetre.mainloop()
