import random


NB_MIN = 1
NB_MAX = 10
NB_MAGIC = random.randint(NB_MIN, NB_MAX)
NB_VIES = 4

def demander_nombre(nb_min, nb_max):
    nb_int = 0
    while nb_int == 0 :
        user_input = input(f"Quel est le nombre magic ( entre {nb_min} et {nb_max} ) ? : ")
        try :
            nb_int = int(user_input)
            
        except ValueError:
            print("UN NOMBRE PARDIS !!!")
            
        else :
            if nb_int < nb_min or nb_int > nb_max :
                print(f"Veuillez entrer un nombre entre {nb_min} et {nb_max}")
                nb_int = 0
    
    return nb_int

"""
--- Boucle While pour les vies ---
vies = NB_VIES
nb = 0
while not nb == NB_MAGIC and not vies == 0 :
    print(f"Vouz avez {vies} vies")
    nb = demander_nombre(NB_MIN, NB_MAX)
    
    if nb == NB_MAGIC:
        print("Bravo, vous avez gagné")
    elif nb > NB_MAGIC:
        print("Le nombre magic est plus petit")
        vies -= 1
    else:
        print("Le nombre magic est plus grand")
        vies -= 1

if vies == 0 :
    print("Vous avez perdu")
    
"""

win = False

for i in range(0, NB_VIES):
    
    nb = demander_nombre(NB_MIN, NB_MAX)
        
    if nb == NB_MAGIC:
            print("Bravo, vous avez gagné")
            win = True
            break
            
    elif nb > NB_MAGIC:
            print("Le nombre magic est plus petit")
    
    else:
            print("Le nombre magic est plus grand")


if win :
    print("Vous avez perdu")