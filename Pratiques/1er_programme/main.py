def ask_age():
    age = 0
    while age == 0:
        age_str = input("Entrez votre âge : ")
        try: 
            age = int(age_str)
        except ValueError:
            print("Vous devez entrer un nombre")
    return age

# ask for name
name = input("Entrez votre nom : ")
while name == "":
    name = input("Ce champ est obligatoire. Veuillez entrer votre nom : ")
    
# ask for age
age = ask_age()

# show the result
print("Bienvenue "+ name + " !" + " Vous avez "+ str(age) + " ans.")
print("l'année prochaine vous aurez " + str(age + 1) + " ans.")