#Auteur : APATA Ruth Esther
#Numéro d'étudiant : 300144673

print ("Auteur : APATA Ruth Esther")
print("Numéro d'étudiant : 300144673")

def jourSemaine(n):
    
        if n==1:
            jour = "Dimanche."
        elif n==2:
            jour ="Lundi."
        elif n==3:
            jour ="Mardi."
        elif n==4:
            jour ="Mercredi."
        elif n==5:
            jour ="Jeudi."
        elif n==6:
            jour ="Vendredi."
        elif n==7:
            jour ="Samedi."
        else:
            jour ="Jour non valide."

        return jour


print(jourSemaine(2))
