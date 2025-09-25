def calculeMoyenne(x):
   m = 0
   for i in x:
      m = m + i
   return m / len(x)

ch = input('Veuillez entrer une liste des valeurs separees par virgules: ')
l1 = list(eval(ch))
print(l1)
print("La moyenne est:",calculeMoyenne(l1)) 
