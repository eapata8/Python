def cherche_m(l, v):
  '''(list, int) -> bool
  Retourne True si v est dans la liste de listes, et False sinon" 
  '''
  NPas = 0
  trouve = False
  for rang_val in l:
    if trouve:
      break
    for col_val in rang_val:
      NPas += 1
      if col_val == v:
          trouve = True
          break
  print("Nombre de pas", NPas)      
  return trouve

N = 100


l1 = [ [1,2,3, 12], [4,5,6], [8,9, 7]]
print(l1)
print(cherche_m(l1, 8))
      

