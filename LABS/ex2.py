def statistiques(x):
    m = 0
    max = x[0]
    min = x[0]
    s = []
    for i in x:
      m = m + i
      if max < i:
        max = i
      if min > i:
        min = i
    m = m / len(x)
    s.append(m)
    s.append(max)
    s.append(min)
    return s

ch = input('Veuillez entrer une liste des valeurs separees par virgules: ')
l1 = list(eval(ch))
print(l1)
l2 = statistiques(l1)
print("Les statistiques sont:")
print("La moyenne:",l2[0]) 
print("Le maximum:",l2[1]) 
print("Le mimimum:",l2[2]) 
