#Auteur : APATA Ruth Esther
#Numéro d'étudiant : 300144673

print("Auteur : APATA Ruth Esther")
print("Numéro d'étudiant : 300144673")

def interactionUtilisateur():  
    prenom = input("Entrez votre prénom: ")
    nom = input("Entrez votre nom: ")
    identifiant = int(input("Entrez votre identifiant à quatre chiffres: "))
 
    if 999 < identifiant <= 9999:
        print("Bonjour " + prenom + " " +nom + ". J'espère que vous allez bien. " + 'Bienvenue dans "mon programme". Votre identifiant est: ' + '"' + str(identifiant) + '"')
    else:
        print("Bonjour " + prenom + " " +nom + ". Veuillez vérifier votre identifiant.")


interactionUtilisateur()
