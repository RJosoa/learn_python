def ask_name():
    name = input("Votre nom ? ")
    while name == "":
        name = input("Veuillez renseigner votre nom ")

    return name
    
    
def ask_age(name):
    age = 0
    while age == 0:
        age_str = input(name + " Entrez votre âge : ")
        try: 
            age = int(age_str)
        except ValueError:
            print(name + " Vous devez entrer un nombre")
    return age

# ask for name
user1 = ask_name()
user2 = ask_name()
    
# ask for age
age1 = ask_age(user1)
age2 = ask_age(user2)

# show the result
print("Bienvenue "+ user1 + " ! ❤️")
print ("Vous avez "+ str(age1) + " ans. 👀")
print("l'année prochaine vous aurez " + str(age1 + 1) + " ans. 😱")
print()
print("Bienvenue "+ user2 + " ! 👋")
print ("Vous avez "+ str(age2) + " ans. ✌️")
print("l'année prochaine vous aurez " + str(age2 + 1) + " ans. 👌")

