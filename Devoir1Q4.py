#Auteur : APATA Ruth Esther
#Numéro d'étudiant : 300144673

print("Auteur: APATA Ruth Esther")
print("Numéro d'étudiant : 300144673")

#Definissons la fonction calculPrix qui retourne le prix d'un article selon sa nature et de la quantite demandée supposant qu'ils sont tous les deux valides
def calculPrix(article,quantite):
    if article == "bureau":
        prix_unitaire = 75.9
    elif article == "chaise":
        prix_unitaire = 50.9
    elif article == "imprimante":
        prix_unitaire = 32.5
    elif article == "scanneur":
        prix_unitaire = 28
    else:
        prix_unitaire = 0
        
    prix = quantite*prix_unitaire

    return prix


#Definissons la foncion calculTotal qui donne le prix total de l'achat tout en supposant que les noms et les quantités sont valides
def calculTotal(article1,quantite1,article2,quantite2,article3,quantite3):
    prix_1 = calculPrix(article1,quantite1)
    prix_2 = calculPrix(article2,quantite2)
    prix_3 = calculPrix(article3,quantite3)
    prix_total = prix_1 + prix_2 + prix_3

    return prix_total


# Definissons une fonction valider article qui vérifie si l'article est vendu au magasin et son stock est suffisant.
def validerArticle(article,quantite):
    if article == "bureau" and quantite <= 9 or article == "chaise" and quantite <= 25 or article == "imprimante" and quantite <= 46 or article == "scanneur" and quantite <= 17:
       return True
    else:
       return False 


#Passons maintenant à la fonction validerCommande qui vérifie que tous les articles sont vendus au magasin et que tous les stocks sont suffisants.
def validerCommande(article1,quantite1,article2,quantite2,article3,quantite3):
    if validerArticle(article1,quantite1)== True and validerArticle(article2,quantite2) == True and validerArticle(article3,quantite3)== True:
        return True
    else:
        return False


#Ecrivons le programme principal
article1 = input("Entrez le premier article: ")
quantite1= int(input("Entrez la quantité de votre premier article: "))
article2 = input("Entrez le deuxième article: ")
quantite2= int(input("Entrez la quantité de votre deuxième article: "))
article3 = input ("Entrez le troisième article: ")
quantite3= int(input("Entrez la quantité de votre troisième article: "))
               
if validerCommande(article1,quantite1,article2,quantite2,article3,quantite3):
    print("Le prix total de votre commande est",calculTotal(article1,quantite1,article2,quantite2,article3,quantite3),"$. Merci et à la prochaine.")
else:
    print("Votre commande est annulée. SVP, vérifier les articles ou les quantités.")
    

    
