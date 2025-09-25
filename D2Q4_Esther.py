#Auteur : APATA Ruth Esther
#Numéro d'étudiant : 300144673

print("Auteur : APATA Ruth Esther")
print("Numéro d'étudiant : 300144673")

#Définissons la fonction palindrome qui prend une chaine de caractères en paramètre et retourne un booléen.
#Ce booléen retourné sera TRUE si la chaine de caractères est un palindrome et FALSE sinon.
def palindrome(chaine):
    n = len(chaine)
    m = n-1
    for var in range(0, n):
        if chaine[var] != chaine[m]:
            return False
        else:
            m = m - 1
    return True

print(palindrome("laval"))


                

