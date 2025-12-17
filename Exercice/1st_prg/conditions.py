''' Consigne: créer des conditions ''' 
# age == 17 : Pousser un petit peu et vous êtes majeur
# age == 18 : Tout juste majeur: Felicitation !!
# age < 18 : Vous êtes mineur
# age >= 18 : Vous êtes majeur
# age > 60 : Vous êtes senior
# age < 10 : Vous êtes bébé
# age == 0 : Vous venez de naître
# age < 0 : Vous devez encore naître
# Adolescent si age >= 12 et age < 18
#        aussi ->  12 <= age < 18
# Bebe si age == 1 ou age == 2

def show_user_information(name, age):
    age_int = int(age)
    print("--- Vos informations ---")
    print("Nom : " + name)
    print("Age : " + str(age_int))
    
    if age_int == 17:
        print("Pousser un petit peu et vous êtes majeur")
        
        ''' condition and et or '''
        ''' & est different de and '''
        ''' | est different de or '''
    elif age_int >= 12 and age_int < 18:
        print("Vous etes adolescent")
    # elif 12 <= age_int < 18:
    #     print("Vous etes adolescent")
    elif age_int == 1 or age_int == 2:
        print("Vous etes bebe")
        
        
    elif age_int == 18:
        print("Tout juste majeur: Felicitation !!")
    elif age_int >= 60:
        print("Vous êtes senior")
    elif age_int <= 10:
        print("Vous êtes enfant")
    elif age_int >= 18:
        print("Vous êtes majeur")
    else :
        print("Vous êtes mineur")


        
show_user_information("John", 2)

