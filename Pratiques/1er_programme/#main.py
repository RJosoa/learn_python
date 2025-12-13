def ask_name():
    name = input("Votre nom ? ")
    while name == "":
        name = input("Veuillez renseigner votre nom ")

    return name
    
    
def ask_age(name):
    age = 0
    while age == 0:
        age_str = input(name + ", quel est votre âge : ")
        try: 
            age = int(age_str)
        except ValueError:
            print("Vous devez entrer un nombre")
    return age
    

def show_user_information (name , age):
    print ()
    print("Bienvenue "+ name + " !")
    print ("Vous avez "+ str(age) + " ans.")
    print("L'année prochaine vous aurez " + str(age + 1) + " ans.")
    
    if age == 17:
        print("Pousser un petit peu et vous êtes majeur")
    elif age == 18:
        print("Tout juste majeur: Felicitation !!")
    elif age == 0:
        print("Vous venez de naître")
    elif age >= 60:
        print("Vous êtes senior")
    elif age <= 10:
        print("Vous êtes bébé")
    elif age >= 18:
        print("Vous êtes majeur")
    else :
        print("Vous êtes mineur")

        
    


# ask for name
name1 = ask_name()
name2 = ask_name()
    
# ask for age
age1 = ask_age(name1)
age2 = ask_age(name2)

# show the result
show_user_information(name1, age1)
show_user_information(name2, age2)