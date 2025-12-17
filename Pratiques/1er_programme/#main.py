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


def ask_size():
    size = 0
    while size == 0:
        size_str = input("Quel est votre taille ? : ")
        try:
            size = float(size_str)
        except ValueError:
            print("Vous devez entrer un nombre")
    return size


def age_condition(age):
    if age == 17:
        print("Pousser un petit peu et vous êtes majeur")
    elif 12 <= age < 18:
        print("Vous etes adolescent")
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
    else:
        print("Vous êtes mineur")


def show_user_information(name, age, size, children):
    print()
    print("Bienvenue " + name + " !")
    print(f"Bienvenue {name} !")
    print("Vous avez " + str(age) + " ans.")
    print("L'année prochaine vous aurez " + str(age + 1) + " ans.")
    print("Vous mesurez %s m" % (size))
    # s'il y a plusieur valeurs a mettre
    # print("Vous vous appellez %s et vous mesurez %s m" % (name, size ))
    if children != 0 :
        print("Vous avez un (des) enfant(s)")

    age_condition(age)


# ask for name
# name1 = ask_name()
# name2 = ask_name()

# ask for age
# age1 = ask_age(name1)
# age2 = ask_age(name2)

# show the result
# show_user_information(name1, age1)
# show_user_information(name2, age2)

NB_PERSON = 1

for i in range(0, NB_PERSON):
    print()
    print("personne " + str(i + 1))
    name = ask_name()
    age = ask_age(name)
    size = ask_size()
    show_user_information(name, age, size, 0)
