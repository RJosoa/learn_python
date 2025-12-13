"""
Premier programme
Formation Python
apprendre la programmation.
"""

nom = input("Quel est votre nom ? ")
age = input("Quel est votre âge ? ")
# nom = "jean"
# age = 24

# essayer
try:
    age_prochain = int(age) + 1
    
# si erreur
except ValueError:
    print("Erreur : L'âge doit être un nombre.")

# sinon
else:
    print("Bonjour " + nom + ", vous avez " + str(age) + " ans.")
    print("L'an prochain vous aurez " + str(age_prochain) + " ans.")

# finalement
finally:
    print("Fin du programme.")
