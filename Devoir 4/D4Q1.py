#Auteurs: Apata Ruth Esther: 300144673
#         Kologo Wendpanga Jean Eliezer:300101810

print("Apata Ruth Esther: 300144673")
print("Kologo Wendpanga Jean Eliezer:300101810")

def calculPrix(article, quantite):
    '''
    (str,int)->float
    
    Retourne le prix d'une quantité d'un article donné.
    '''
    return (p[article]*quantite)

def calculTotal(article1, quantite1, article2, quantite2, article3, quantite3):
    '''
    (str,int,str,int,str,int)-> float
    
    Retourne le coût total de la commande.
    '''
    return(calculPrix(article1, quantite1)+calculPrix(article2, quantite2)+calculPrix(article3, quantite3))

def validerCommande(article1, quantite1, article2, quantite2, article3, quantite3):
    '''
    (str,int,str,int,str,int)-> bool
    
    Retourne True si tous les articles de la commande et leurs quantités sont valides et false sinon.
    Elle actualise les quantités disponibles dans l’inventaire si la commande est valide.
    '''
    
    commande ={article1:quantite1, article2:quantite2, article3:quantite3}
    
    verif = True
    for var in commande:
        if not(var in q) or commande[var] > q[var] :#vérifie si tous les articles de la commande existent et en quantité suffisante.
            verif = False
            break
        
    if verif == True: #Dans le cas où la commande est validée, l'inventaire s'actualise. 
        for i in commande:
            q[i] -= commande[i]
    return verif

#Programme principal

q = {"bureau":9, "chaise":25, "imprimante":46, "scanneur":17}
p = {"bureau":75.9, "chaise":50.9, "imprimante":32.5, "scanneur":28.0}

article1=str(input("Entrez le premier article: "))   
while True:
    try:
        quantite1=int(input("Entrez la quantité de votre 1er article: "))
        break
    except ValueError:
        print ('Essayez des valeurs entières svp')
        
article2=str(input("Entrez le deuxième article: "))
while True:
    try:
        quantite2=int(input("Entrez la quantité de votre 2eme article: "))
        break
    except ValueError:
        print ('Essayez des valeurs entières svp')
        
article3=str(input("Entrez le troisième article: "))
while True:
    try:
        quantite3=int(input("Entrez la quantité de votre 3eme article: "))
        break
    except ValueError:
        print ('Essayez des valeurs entières svp')
        
print()

if validerCommande(article1, quantite1, article2, quantite2, article3, quantite3)==False:
    print("Votre commande est annulée. SVP, vérifier les articles ou les quantités.")
else:
    print("Le prix total de votre commande est : ",calculTotal(article1, quantite1, article2, quantite2, article3, quantite3)," $. Merci et à la prochaine.")
print()

print("Les quantités disponibles après l'achat sont: ")
print(q)
    
