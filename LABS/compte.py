import random

def compte(l, v):
  '''(list, int) -> int
  Compte le nombre d'occurrence de v est dans la liste" 
  '''
  NPas = 0
  compteur = 0
  for val in l:
      NPas += 1
      if val == v:
          compteur += 1
  print("Nombre de pas", NPas)      
  return compteur

N = 100
    
# liste avec des elements aleatoires
l3 = []
for i in range(N):
  v = random.randrange(1,N+1)
  l3.append(v)
print(l3)
print(compte(l3, 3))
