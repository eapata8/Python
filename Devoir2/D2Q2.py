#Auteur : APATA Ruth Esther
#Numéro d'étudiant : 300144673

print("Auteur : APATA Ruth Esther")
print("Numéro d'étudiant : 300144673")

#Definissons la fonction fibonacci en fonction d'un entier n supérieur ou égal à 2 et qui afficher les n valeurs de la suite de Fibonacci(no et n1 inclues).
def fibonacci(n):
    n0 = 0
    n1 = 1
    n2 = n0 + n1
    print(n0, end = " ")
    print(n1, end = " ")
    
    for var in range(0,n-2):
        print(n2, end = " ")
        n0 = n1
        n1 = n2
        n2 = n0 + n1


#Écrivons le programme principal qui demande à l’utilisateur d’entrer le nombre de termes et qui vérifie que le nombre est supérieur à 2.
n = int(input("Entrez le nombres de termes de la suite de Fibonacci de votre choix. "))
while n <= 2:
    n = int(input("Entrez le nombres de termes de la suite de Fibonacci de votre choix. "))

fibonacci(n)
