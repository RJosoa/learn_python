def show_user_information(name, age):
    print()
    print("--- Vos informations ---")
    print("Nom : " + name)
    print("Age : " + str(age))
    
    age_condition(age)
    
def age_condition(age):
    if age == 17:
        print("Pousser un petit peu et vous êtes majeur")
        
        ''' condition and et or '''
        ''' & est different de and '''
        ''' | est different de or '''
    elif age >= 12 and age < 18:
        print("Vous etes adolescent")
    # elif 12 <= age < 18:
    #     print("Vous etes adolescent")
    elif age == 1 or age == 2:
        print("Vous etes bebe")
        
        
    elif age == 18:
        print("Tout juste majeur: Felicitation !!")
    elif age >= 60:
        print("Vous êtes senior")
    elif age <= 10:
        print("Vous êtes enfant")
    elif age >= 18:
        print("Vous êtes majeur")
    else :
        print("Vous êtes mineur")
            
def ask_user_information():
    NB_PARTITIPATION = 0
    while NB_PARTITIPATION == 0:
        try :
            NB_PARTITIPATION = int(input("Vous etes combien ? "))
        except ValueError:
            print("Entrez un nombre !!")
            
    for i in range(0, NB_PARTITIPATION):
        print()
        print("Personne " + str(i+1))
        name = input("Quel est votre nom ? ")
        age = 0
        while name == "":
            name = input("Veuillez entrer un nom !!")
    
        while age == 0:
            age_str = input("et votre age ? ")
            try :
                age = int(age_str)
            except ValueError:
                print("vous devez entrer un nombre")
                
        
        show_user_information(name, age)
        
        
ask_user_information()

