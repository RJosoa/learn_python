''' Consigne: créer une fonction ''' 
# le nom de la fonction est "demander_nom"
# je dois utiliser une variable "reponse_nom"
# ne pas oublier de faire un return

def demander_nom():
    nom = input("Votre nom ? ")
    while nom == "":
        nom = input("Veuillez renseigner votre nom ")

    return nom
    
response_nom = demander_nom()

print(" Bienvenue " + response_nom + " ❤️")
    
