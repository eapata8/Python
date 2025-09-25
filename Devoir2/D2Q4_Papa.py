#Déterminons la longueur de la chaine

Chaine = input("Entrez votre mot: ")
longueur=len(Chaine)


#Comparons deux caractères symétriques à partir d'une position i gâce à la fonction symetrique
def symetrique(i):
    return Chaine[i] == Chaine[longueur-1-i]
 
    

#Vérifions si tous les caractéres symétriques dans la chaine sont identiques grâce à la fonction
def palindrome(Chaine):
    
    #Initialisation
    i=0
    valeur="true"
    
    #Itérations
    while (longueur-1)>=2*i:
        valeur = valeur and symetrique(i)
        i=i+1

    #Affectation
    return valeur

   
print(palindrome(Chaine))

