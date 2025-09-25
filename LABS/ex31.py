def somme_de_trois(x):
     '''(tuple)->bool
     Retourne True si la somme de 3 elements consecutive est zero
     Precondition: le tuple a au moins 3 elements
     >>> t = (1,2,-3,4,-1,3)
     >>> somme_de_trois(t)
     True
     '''
     res = False
     i = 0
     somme = 0
     while (i < len(x) - 2):
       somme = somme + x[i] + x[i+1] + x[i+2]
       if (somme == 0):
         res = True
         break
       i = i + 1
     return res

t = (1,2,-3,4,-1,3)
print(somme_de_trois(t))


     
