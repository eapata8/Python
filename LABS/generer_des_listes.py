import random

N = 100000

# liste en ordre ascendante de 1 a N
l1 = [ v for v in range(1, N+1) ]
print(l1)

# liste en ordre descendate de N a 1
l2 = [ v for v in range(N, 0, -1) ]
print(l2)

# liste avec des elements aleatoires
l3 = []
for i in range(N):
  v = random.randrange(1,N+1)
  l3.append(v)
print(l3)  
