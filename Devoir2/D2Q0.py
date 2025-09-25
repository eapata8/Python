#Auteur : APATA Ruth Esther
#Numéro d'étudiant : 300144673

print("Auteur : APATA Ruth Esther")
print("Numéro d'étudiant : 300144673")

#Définissons la fonction unites qui permet d’afficher sur 4 lignes le chiffre à chacune des positions d'un nombre donné.
def unites(nombre):
        n = len(nombre)
        print("Le nombre de milliers est:", nombre[0])
        print("Le nombre de centaines est:", nombre[1])
        print("Le nombre de dizaines est:", nombre[2])
        print("Le nombre d'unités est:", nombre[3]) 
    
unites("1309898")
