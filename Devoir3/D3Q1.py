#Auteur: Apata Ruth Esther
#Numéro d'étudiant: 300144673
print("Auteur: Apata Ruth Esther")
print("Numéro d'étudiant: 300144673")

def  nombreDivisibles(a,n):
    '''
     (list,int)-> int

     retourne le nombre d’éléments divisible par n trouvés dans la liste.
     '''
    
    compteur = 0 #On initialise le nombre d'éléments de la liste a divisibles par n à 0.
    for i in a:
        if i%n == 0:
            compteur = compteur + 1 #Le compteur s'incrémente à chaque fois qu'on trouve un multiple de n dans la liste.
    return compteur

liste = input("Veuillez entrer une liste des entiers par des virgules: ")
a = list(eval(liste))
n = int(input("Veuillez entrer un entier positif: "))


print("Le nombre des éléments divisibles par "+ str(n) + " est: " + str(nombreDivisibles(a,n)))

    
