#Auteur : APATA Ruth Esther
#Numéro d'étudiant : 300144673

print("Auteur : APATA Ruth Esther")
print("Numéro d'étudiant : 300144673")

#Définissons la fonction obtenirCodePrime qui retourne le groupe dans lequel le joueur se trouve en fonction de ses statistiques.
def obtenirCodePrime(buts, aides, penalites, matchs, experience):
        if buts > 20 or aides >25 or penalites < 25 and experience >= 5 and matchs > 55:
            return 3
        elif buts > 20 or aides >25 or penalites < 25 and experience >= 5 and matchs <= 55:
            return 2
        elif buts > 20 or aides >25 or penalites < 25 and experience < 5:
            return 1
        else:
            return 0


#Ecrivons le programme principal qui demande les statistiques du joueur et affiche le code de prime du joueur lorsque les données sont correctes.
buts = int(input("Combien de buts avez-vous marqué pendant la saison régulière? "))
aides = int(input("Combien d'aides avez-vous récoltées pendant la saison régulière? "))
penalites = int(input("Combien de pénalités avez-vous obtenues pendant la saison régulière? "))
experience = int(input("Combien d'années avez-vous passées dans l'équipe? "))
matchs = int(input("Vous avez assisté à combien de matchs? "))

while buts < 0:
        print ("Les nombres entrés doivent être positifs. Veuillez réessayer s'il vous plaît.")
        buts = int(input("Combien de buts avez-vous marqué pendant la saison régulière? "))
while aides < 0:
        print ("Les nombres entrés doivent être positifs. Veuillez réessayer s'il vous plaît.")
        aides = int(input("Combien d'aides avez-vous récoltées pendant la saison régulière? "))
while penalites < 0:
        print ("Les nombres entrés doivent être positifs. Veuillez réessayer s'il vous plaît.")
        penalites = int(input("Combien de pénalités avez-vous obtenues pendant la saison régulière? "))
while matchs < 0:
        print ("Les nombres entrés doivent être positifs. Veuillez réessayer s'il vous plaît.")
        matchs = int(input("Vous avez assisté à combien de matchs? "))
while experience < 0:
        print ("Les nombres entrés doivent être positifs. Veuillez réessayer s'il vous plaît.")
        experience = int(input("Combien d'années avez-vous passées dans l'équipe? "))


print ("Votre code de prime est: ",obtenirCodePrime(buts, aides, penalites, matchs, experience))

    
    
