" Consigen :former un escalieur de avec la tortue "

# 1er ex:
# 30px sur x et y
# 5 marge
# 
# 2ème ex:
# Faire une fonction
# escalier(taille, nb_repetition)

import turtle

t= turtle.Turtle()

def escalier(taille, nb):
    for i in range(0,nb):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
        
        # faire evoluer la taille de -5 durant chaque boucle
        # taille = taille - 5 or
        taille -= 5 
    t.forward(taille)
    

escalier(60, 10)
turtle.done()