#Auteurs: Apata Ruth Esther: 300144673
#         Kologo Wendpanga Jean Eliezer:300101810

print("Apata Ruth Esther: 300144673")
print("Kologo Wendpanga Jean Eliezer:300101810")

from math import sqrt
def modifierMat(matrice): 
    '''
    (list)->(list)
    
    Prend en paramètres une matrice et retourne une matrice de mêmes dimensions
    tout en remplaçant les nombres paires de cette matrice en leurs racines carrées.
    '''
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j]%2==0:
                matrice[i][j]= sqrt(matrice[i][j])
    return matrice
 
matrice = [[5, 3, 8], [7, 4, 6], [1, 9, 2], [8, 7, 1], [3, 2, 9], [4, 6, 5]]
print(modifierMat(matrice))
