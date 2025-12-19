TO_CM = 2.54
TO_INCHES = 0.394

def conversion():
    print("--- Conversion entre cm et pouces ---")
    print("Rappel :")
    print(f"1 pouce = {TO_CM} cm")
    print(f"1 cm = {TO_INCHES} pouce")
    print()
    print("Qu'est ce que vous voulez convertir ? :")
    print("n°1 : pouces vers cm")
    print("n°2 : cm vers pouces")
    
    choice = 0
    # On utilise True pour boucler jusqu'à avoir une réponse valide
    while True:
        user_input = input("-> n°")
        try:
            choice = int(user_input)
            if choice == 1 or choice == 2:
                break # On sort de la boucle car le choix est valide
            else:
                print("Veuillez choisir 1 ou 2 !")
        except ValueError: 
            print("Veuillez écrire un nombre entier (1 ou 2) !")
                
    print()
    
    value_to_convert = 0.0
    while True:
        print("La valeur à convertir : ")
        value_str = input("-> ")
        try:
            value_to_convert = float(value_str)
            break # On sort de la boucle car la valeur est valide
        except ValueError: 
            print("Erreur. Veuillez entrer un nombre valide (utilisez le point . pour les décimales).")
        print()
        
    # Calcul et affichage
    if choice == 1:
        result = value_to_convert * TO_CM
        unit_src = "pouces"
        unit_dest = "cm"
    else:
        result = value_to_convert * TO_INCHES
        unit_src = "cm"
        unit_dest = "pouces"

    # Affichage final
    print(f"Conversion de {value_to_convert} {unit_src} vers {unit_dest}")
    print(f"{value_to_convert} {unit_src} = {round(result, 2)} {unit_dest}")


# Boucle principale du programme
while True:
    conversion()
    
    print()
    print("Une autre conversion ? (o/n)")
    
    reponse_valide = False
    while not reponse_valide:
        response = input("-> ").lower() # .lower() met tout en minuscule pour simplifier
        
        if response in ["o", "oui"]:
            reponse_valide = True
            # On ne fait rien, la boucle principale (while True) va recommencer
            
        elif response in ["n", "non"]:
            print("// A bientôt // 👋")
            exit() # On quitte tout le programme
            
        else:
            print("Veuillez répondre par 'o' ou 'n'")
    print("-" * 30)
    print()