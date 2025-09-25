def calculeTriagleSup(m):
  ''' (list) -> list
       retourne la somme des elements du traigle superieur
       Precondition: m est une liste de listes des entiers 
  '''
  somme = 0 
  L = 0
  while L < len(m):
     C = 0
     while C < len(m[L]):
        if L <= C:
          somme = somme + m[L][C]
        C = C + 1
     L = L + 1
  return somme  

print(calculeTriagleSup([[1,2],[3,4]]))
