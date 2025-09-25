def Produit_de_1_a_N(N):
    compteur = 1
    produit = 1
    while compteur <= N:
        produit = produit*compteur
        compteur = compteur + 1
    print (produit)

Nombre = int(input("Entrez le nombre svp "))
Produit_de_1_a_N(Nombre)
