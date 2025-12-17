" Consigen :former des carrés dans un carré sous differente taille"

# Faire une fonction
# carres(taille_depart, nb_carré)

import turtle

t = turtle.Turtle()

def carre(taille):
    for i in range(0, 4):
        t.forward(taille)
        t.left(90)
        

# def carres(taille_depart, nb):
#     for i in range (0, nb):
#         carre(taille_depart )
#         taille_depart = taille_depart + nb
        
        
def carres(taille_depart, nb):
    for i in range (0, nb):
        taille = (i+1)*taille_depart
        carre(taille )
    
carres(10, 5)

turtle.done()