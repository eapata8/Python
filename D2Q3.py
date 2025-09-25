#Auteur : APATA Ruth Esther
#Numéro d'étudiant : 300144673

print("Auteur : APATA Ruth Esther")
print("Numéro d'étudiant : 300144673")

#Définissons une fonction triangle qui permet d’afficher un triangle isocèle formé du caractère ‘*’en prenant en entrée sa hauteur.
def triangle(hauteur):
    etoiles = 1
    espaces1 = hauteur - 1
    espaces2 = hauteur - 1 
    
    for var in range (0, hauteur):
        for var2 in range (0, espaces1):
            print(" ", end = " ")
        for var3 in range (0, etoiles):
            print ("*", end = " " )
        for var4 in range (0, espaces2):
            print(" ", end = " ")
        print(" ")
        espaces1 = espaces1 - 1
        etoiles = etoiles + 2
        espaces2 = espaces2 - 1


triangle(8)
	
