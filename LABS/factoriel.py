# factoriel 1 * 2 * ... * n
# 0! = 1
# avec des fonctions

def calculeFact(n):
 fact = 1
 compteur = 1
 while compteur <= n:
  fact = fact * compteur
  compteur = compteur + 1
 return(fact)

n = -1 
while(n < 0):
 n = int(input("Veuillez entrer n, un entier non-negatif: "))
 if (n < 0):
   print("n doit etre non-negatif")

print('Le factoriel est', calculeFact(n)) 
 
