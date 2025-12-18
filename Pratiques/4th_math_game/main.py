import random

MIN_NUMBER = 1
MAX_NUMBER = 10
NB_QUESTION = 4

def ask_question():
    nb_min = MIN_NUMBER
    nb_max = MAX_NUMBER
    

    a = random.randint(nb_min, nb_max)
    b = random.randint(nb_min, nb_max)
    o = random.randint(0, 1)
    operator = "*"
    if o == 0 : 
        operator = "+"
    else :
        operator = "*"
        
    print(f"Calculer {a} {operator} {b} : ")
    user_input = input("-> ")
    
    if o == 0 : 
        calcule = a + b
    else :
        calcule = a * b
        
    nb_int = int(user_input)
    
    if nb_int == calcule :
        return True
            
    else :
        return False
        
    
    
nb_point = 0       
for i in range (0, NB_QUESTION) :
    print(f"Question n°{i+1} sur {NB_QUESTION} ")
    # print(f"Vous avez : {nb_point} pts")

    if ask_question() :
        print("reponse correct")
        nb_point += 1
        
    else :
        print("reponse incorrect")
        
    print()
    
print(f"Votre note est : {nb_point} / {NB_QUESTION}")
moyenne = int(NB_QUESTION/2)

if nb_point == NB_QUESTION :
    print("EXCELENT")
    
elif nb_point == 0 :
    print("Révisez vos Maths !")
    
elif nb_point > moyenne :
    print ("Pas mal !")
    
else :
    print("Peux mieu faire")