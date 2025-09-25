
def palindrome(Chaine):
    longueur=len(Chaine)
    #Initialisation
    i=0
    valeur="true"
    
    #Itérations
    while (longueur-1)>=2*i:
        valeur = valeur and Chaine[i] == Chaine[longueur-1-i]
        i=i+1

    #Affectation
    return valeur

   
print(palindrome("apatapa"))

