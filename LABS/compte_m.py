def compte_m(l, v):
  '''(list, int) -> int
  Retourne le nombre d'occurence de v est dans la liste de listes" 
  '''
  NPas = 0
  compteur = 0
  for rang_val in l:
    for col_val in rang_val:
      NPas += 1
      if col_val == v:
          compteur += 1
  print("Nombre de pas", NPas)      
  return compteur

N = 100

l1 = [ [1,2,3,8], [4,5,6,8,7], [8,9,60]]
print(l1)
print(compte_m(l1, 8))
      

