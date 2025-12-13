''' Consigen: créer une finction '''
# afficher_informations_personne
# Paramètres: nom, age

def show_user_information(name, age):
    age_int = int(age)
    print("--- Vos informations ---")
    print("Nom : " + name)
    print("Age : " + str(age_int))

    return name, age
    
show_user_information("John", 32)
    
