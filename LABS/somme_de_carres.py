# 1*1 + 2*2 + ... + n*n

def sommeDeCarees(n):
 valeur = 1
 somme = 0
 while valeur <= n:
   somme = somme + valeur * valeur
   valeur = valeur + 1
 return somme  


n = int(input("Veuillez entrer n "))
print(sommeDeCarees(n)) 
 
