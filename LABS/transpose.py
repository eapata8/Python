def transpose(m):
  ''' (list) -> list
       Precondition: m est une matrice m x n
       Le resultat est une matrice n x m
  '''
  C = 0
  m1 = []
  while C < len(m[0]):
     L = 0
     m1.append([])
     while L < len(m):
        m1[C].append(m[L][C])
        L = L + 1
     C = C + 1
  return m1

L = [[1,2,3],[4,5,6]]
L1 = transpose(L)
print(L1)
