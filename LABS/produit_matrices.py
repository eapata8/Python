def produit_matrices(m1, m2):
  ''' (list, list) -> list
       retourne le produit des 2 matrice
       Preconditions: m1 de dimensions m x n, m2 de dimensions n x p
       le resultat est une matice de dimensions m x p
  '''
  i = 0
  m3 = []
  while i < len(m1):
     j = 0
     m3.append([])
     while j < len(m2[0]):
        k = 0
        m3[i].append(0)
        while k < len (m1[0]): 
           m3[i][j] += m1[i][k] * m2[k][j]
           k = k + 1 
        j = j + 1
     i = i + 1
  return m3   

print(produit_matrices([[1,2,3],[4,5,6]], [[1,2],[3,4],[5,6]]))

