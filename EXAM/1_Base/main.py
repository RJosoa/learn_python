TO_CM = 2.54
TO_INCHES = 0.394

def conversion() :
    print("--- Convesion entre cm et pouces ---")
    print("Rappelle :")
    print(f"1 pouce = {TO_CM} cm")
    print(f"1 cm = {TO_INCHES} pouce")
    print()
    print("Qu'est ce que vous voulez convertir ? :")
    print("n°1 : pouces vers cm ?")
    print("n°2 : cm vers pouces ?")
    
    num_int = 0
    while num_int == 0  :
        user_input = input("-> n°")
        try :
            num_int = int(user_input)
            if num_int < 1 or num_int > 2 :
                print()
                print("Veuillez choisir 1 ou 2 !")
                num_int = 0
                
        except ValueError: 
            print()
            print("Veuillez ecrire un nombre !")
                
    print()
    value_int = 0
    while value_int == 0 :
        print("La valeur a convertir : ")
        value_str = input("-> ")
        try :
            value_int = float(value_str)
            
        except ValueError: 
            print("Erreur. Veuillez choisir des chiffres et utilisez le . au lieu d'une ,")
        
        print()
        
    if num_int == 1 :
        print(f"Convertion de {value_int} pouces vers cm")
        result = float(value_int * TO_CM)
        result_round = round(result, 2)
        return print(f"{value_int} pouces = {result_round} cm")
            
    elif num_int == 2 :
        print(f"Convertion de {value_int} cm vers pouces")
        result = float(value_int * TO_INCHES)
        result_round = round(result, 2)
        return print(f"{value_int} cm = {result_round} pouces")
            
    else :
        print("Error")
        
    

restart = True
while restart :
    conversion()
    print()
    print("Un autre convertion ?")
    print("répondez par o (oui) ou n (non)")
    
    x = 0
    while x == 0 :
        response = input("-> ")
        try : 
            if response == "o" or response ==  "oui" :
                print("oui")
                corect = True
                
            elif response == "n" or response == "non" :
                print("non")
                restart = False
                break
                
            else :
                print("soit o ou n")
                x = 0
                print()
        
        except :
            print("ERROR")   
    
    print()     
    print ("// A bientôt // 👋")
