def show_user_information(name, age):
    age_int = int(age)
    print("--- Vos informations ---")
    print("Nom : " + name)
    print("Age : " + str(age_int))
    
    if age_int == 17:
        print("Pousser un petit peu et vous êtes majeur")
    elif age_int == 18:
        print("Tout juste majeur: Felicitation !!")
    elif age_int < 18:
        print("Vous êtes mineur")
    else:
        print("Vous êtes majeur")
        
show_user_information("John", 17)