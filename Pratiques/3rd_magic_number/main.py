NB_MIN = 1
NB_MAX = 10
NB_MAGIC = 5

def condition_nombre(nb_magic, nb_str):
    try :
        nb = int(nb_str)
        if nb == nb_magic:
            print("Bravo, vous avez gagné")
        elif nb > nb_magic  :
            print("Le nombre magic est plus petit")
        else :
            print("Le nombre magic est plus grand")        
    except ValueError :
        print("UN NOMBRE PARDIS !!!")



def demander_nombre (nb_min, nb_max) :
    nb = 0
    while nb != NB_MAGIC:
        
        nb = input(f"Quel est le nombre magic ( entre {nb_min} et {nb_max} ) ? : ")

        condition_nombre(NB_MAGIC, nb)


    
    
demander_nombre(NB_MIN, NB_MAX)

