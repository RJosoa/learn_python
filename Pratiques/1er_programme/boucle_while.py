# n = 0
# while n < 10:
#     print("Valeur de n :", n)
#     n += 1
    
# print("Fin du programme")

password = ""
while password != "toto":
    password = input("Entrez le mot de passe : ")
    
    if password == "toto":
        print("Mot de passe correct")
    else:
        print("Mot de passe incorrect")
        print("Veuillez réessayer")

print("Fin du programme")