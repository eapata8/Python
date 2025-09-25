import random

def cherche(l, v):
  '''(list, int) -> bool
  Retourne True si v est dans la liste, et False sinon" 
  '''
  NPas = 0
  trouve = False
  for val in l:
      NPas += 1
      if val == v:
          trouve = True
          break
  print("Nombre de pas", NPas)      
  return trouve

N = 100

# liste en ordre ascendant de 1 a N
l1 = [ v for v in range(1, N+1) ]
print(l1)
print(cherche(l1, 78))
      
# liste avec des elements aleatoires
l3 = []
for i in range(N):
  v = random.randrange(1,N+1)
  l3.append(v)
print(l3)
print(cherche(l3, 78))
