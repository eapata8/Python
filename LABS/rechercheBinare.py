def recherche_binaire(L, v):
  """ (list, int) -> bool
  Retourne True si v est dans la liste trie L, et False sinon.
  >>> recherche_binaire([1, 2, 3, 4, 4, 5, 7, 9, 10, 13], 10)
  Nombre de pas 3
  True
  >>> recherche_binaire([1, 2, 3, 4, 4, 5, 7, 9, 10, 13], 6)
  Nombre de pas 4
  False
  """
  NPas = 0
  trouve = False
  # i et j delimitent la section de recherche
  i = 0
  j = len(L) - 1 
  while i != j + 1:
    NPas += 1
    m = (i + j) // 2  # trouve le milieu
    if L[m] == v:   # si on a trouve, retourne la position
      trouve = True
      break
    elif L[m] < v:  # fouille a la droite 
      i = m + 1
    else:           # fouille a la gauche
      j = m - 1
  print ("Nombre de pas", NPas)    
  return trouve
