" Consigen :former un carre "

# Faire une fonction
# carre(taille)


import turtle

t = turtle.Turtle()

def carre(taille):
    for i in range(0, 4):
        t.forward(taille)
        t.left(90)


carre(100)
turtle.done()