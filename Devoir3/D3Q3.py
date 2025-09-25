#Auteur: Apata Ruth Esther
#Numéro d'étudiant: 300144673
print("Auteur: Apata Ruth Esther")
print("Numéro d'étudiant: 300144673")

def sequenceMax(a):
'''
(list)-> int

Retourne la longueur de la plus longue séquence d’éléments consécutifs égaux
ou 1 s’il n’y a aucune séquence.
'''

    compteur = 1 #On intialise le nombre d'éléments consécutifs identiques à 1.
    result = 1 #On intialise le plus grand nombre d'éléments consécutifs identiques à 1.
    liste = [] #Créons une liste vide qui va se remplir progressivement avec les différentes valeurs du compteur.
    for i in range(len(a)-1):
        if a[i]==a[i+1]:
            compteur = compteur + 1#Le compteur s'incrémente lorsqu'il y a deux éléments consécutifs identiques.
        else:
            compteur = 1 #Lorsque le prochain élément est différent, le compteur revient à 1
        liste.append(compteur)        
    for var in liste: #Cette boucle permet de trouver le plus grand compteur
        if var>=result:
            result = var
    return result

liste = input("Veuillez entrer une liste des entiers par des virgules: ")
a = list(eval(liste))
print(sequenceMax(a))
