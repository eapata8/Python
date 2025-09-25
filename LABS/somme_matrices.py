def somme_matrices(m1, m2):
  ''' (list, list) -> list
       retourne une liste ou chanque element est la somme des elements
       de m1 et m2 dans la meme position
       Precondition: m1, m2 sont des listes de listes des entiers avec la meme taille
  '''
  i = 0
  m3 = []
  while i < len(m1):
     j = 0
     m3.append([])
     while j < len(m1[i]):
        m3[i].append(m1[i][j] + m2[i][j])
        j = j + 1
     i = i + 1
  return m3   



print(somme_matrices([[1,2],[3,4]], [[1,1],[1,1]]))
