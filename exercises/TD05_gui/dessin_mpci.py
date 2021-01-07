import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk ## Importation des modules utiles dans PIL
from random import *
######################################################################################################################################
root = tk.Tk()
root.title("titre")

#Construction d'une variable de contrôle qui stocke une chaine de caractère
couleur_utilisateur = tk.StringVar()
#1 Pour connaitre la valeur de couleur utilisateur on utilise la méthode get()
# couleur_utilisateur.get() <--- retourne une chaine de caractere
#2 Pour modifier la valeur de couleur utilisateur on utilise la méthode set()
# couleur_utilisateur.set( ARGUMENT ) 

couleur_utilisateur.set("yellow")

image = Image.open("/Users/axelmathieu-mahias/Desktop/carre.png") 
image = image.resize((30,30), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image) 

cercle = Image.open("/Users/axelmathieu-mahias/Desktop/cercle.png") 
cercle = cercle.resize((30,30), Image.ANTIALIAS)
photo_cercle = ImageTk.PhotoImage(cercle) 

croix = Image.open("/Users/axelmathieu-mahias/Desktop/croix.png") 
croix = croix.resize((30,30), Image.ANTIALIAS)
photo_croix = ImageTk.PhotoImage(croix) 

couleur = Image.open("/Users/axelmathieu-mahias/Desktop/couleur.png") 
couleur = couleur.resize((100,100), Image.ANTIALIAS)
photo_couleur = ImageTk.PhotoImage(couleur) 

#Creation d'une fonction qui doit afficher un cercle aleatoire dans le canvas
def affiche_cercle():
   x = randint(75, 525)
   y = randint(75, 525)
   canvas.create_oval(x,y, x+50, y+50, fill= couleur_utilisateur.get())

def affiche_carre():
   x = randint(75, 525)
   y = randint(75, 525)
   canvas.create_rectangle(x,y, x+50, y+50, fill= couleur_utilisateur.get() )

def affiche_croix():
   x = randint(75, 525)
   y = randint(75, 525)
   canvas.create_rectangle(x,y, x+50, y+50, fill = couleur_utilisateur.get(), outline = "yellow")
   canvas.create_line(x,y, x+50, y + 50, fill = "yellow")
   canvas.create_line(x+50,y, x, y + 50, fill = "yellow")

def choisir_couleur():
    couleur_utilisateur.set(input("Veuillez choisir une couleur : "))


#CREATION
font1 = tkFont.Font(family='Meiryo', size=20, weight='bold')
font2 = tkFont.Font(family='Kohinoor Gujarati', size=20, weight='bold')
font3 = tkFont.Font(family = 'Futura', size = 20, weight = 'bold')
font4 = tkFont.Font(family = 'Century', size = 20, weight = 'bold')

bouton_cercle = tk.Button(text = "Cercle", borderwidth = "5m", font = font1, fg = "yellow", command = affiche_cercle, image = photo_cercle, relief = "sunken", width = 50)
bouton_carre = tk.Button(text= "Carre",borderwidth = "5m", font = font2, fg = "green", command = affiche_carre, image = photo, relief = "sunken", width = 50)
bouton_croix = tk.Button(text="Croix", borderwidth = "5m", font = font3, fg = "blue", command = affiche_croix, image =  photo_croix, relief = "sunken", width = 50)
bouton_couleur = tk.Button(text="Choisir une couleur",borderwidth = "1c", font = font4, fg = "red", command = choisir_couleur, image = photo_couleur, relief = "sunken", width = 150)


canvas = tk.Canvas(background = "#000000", borderwidth = "1c", relief = "ridge", width = 600, height = 600, cursor = "pirate")

#PLACEMENT
bouton_cercle.grid(row = 1, column = 0)
bouton_carre.grid(row = 2, column = 0)
bouton_croix.grid(row = 3, column = 0)
bouton_couleur.grid(row = 0, column = 2)

canvas.grid(row = 1, column = 1, rowspan = 3, columnspan = 3)


######################################################################################################################################
# Fin de votre code
root.mainloop()