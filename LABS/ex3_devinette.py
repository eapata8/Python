# jeu de devinette
import random

def devine(n):
    # VARIABLE INTERMÉDIAIRES
    nbrDeviné = 0  # le nombre deviné par l'utilisateur
                   # initialisee avec une valuer invalide dans le jeu 
    # VARIABLE RESULTAT
    tentatives = 1
    while(nbrDeviné != n):
      nbrDeviné = int(input("S.V.P. devinez le numéro: "))     
      if(nbrDeviné != n):
        tentatives = tentatives+1;
        if(nbrDeviné > n):
            print("Trop haut")
        else:
            print("Trop bas")
    # RETOURNER LE RÉSULTAT
    return(tentatives)


n = random.randrange(1,11)
#n = random.randint(1, 10) 
#print(n)

# APPEL DE LA MÉTHODE DE RÉSOLUTION DE PROBLÈME
nbrTentatives = devine(n)
# AFFICHAGE DES RÉSULTATS ET MODIFIÉES À L'ÉCRAN
print("Bravo! Vous avez trouvé le numéro en", nbrTentatives,"tentatives.")
