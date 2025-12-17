nom = "toto"
age = 17

print("Je suis "+ nom + " et j'ai " + str(age) +" ans. ")

# "=/= de concatener, on passe juste les arguments"
print("Je suis",nom,"et j'ai",age,"ans. ")

# Chaine formatée
print(f"Je suis {nom} et j'ai {age} ans. " )
# or
print("Je suis %s et j'ai %s ans. "% (nom, age))

# Je passe ce que je veux sous n'importe quelle ordre
print(f"""
Ici,
    je
        peux
            coller
    ce 
que je veux.
        Je 
        suis {nom}, 
    er j'ai
                %s ans.
                
    """ % (age))