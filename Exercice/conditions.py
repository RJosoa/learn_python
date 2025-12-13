''' Consigne: créer des conditions ''' 
# age == 17 : Pousser un petit peu et vous êtes majeur
# age == 18 : Tout juste majeur: Felicitation !!
# age < 18 : Vous êtes mineur
# age >= 18 : Vous êtes majeur
# age > 60 : Vous êtes senior
# age < 10 : Vous êtes bébé
# age == 0 : Vous venez de naître
# age < 0 : Vous devez encore naître

def show_user_information(name, age):
    age_int = int(age)
    print("--- Vos informations ---")
    print("Nom : " + name)
    print("Age : " + str(age_int))
    
    if age_int == 17:
        print("Pousser un petit peu et vous êtes majeur")
    elif age_int == 18:
        print("Tout juste majeur: Felicitation !!")
    elif age_int == 0:
        print("Vous venez de naître")
    elif age_int >= 60:
        print("Vous êtes senior")
    elif age_int <= 10:
        print("Vous êtes bébé")
    elif age_int >= 18:
        print("Vous êtes majeur")
    else :
        print("Vous êtes mineur")


        
show_user_information("John", 0)

