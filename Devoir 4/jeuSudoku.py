#Auteurs: Apata Ruth Esther: 300144673
#         Kologo Wendpanga Jean Eliezer:300101810
def verifierLigne(grille, row, num):
    '''
        (list, int, int) -> Bool
        Vérifier si la case à ajouter n'existe pas sur la ligne.
        Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''
    # A COMPLETER
    v = True
    i = 0
    while i < len(grille):
        if grille[row][i] == num:
            v = False
        i = i + 1

    return v

def verifierCol(grille, col, num):
    '''
            (list, int, int) -> Bool
            Vérifier si la case à ajouter n'existe pas sur la colonne.
            Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''
    # A COMPLETER
    v = True
    i = 0
    while i < len(grille):
        if grille[i][col] == num:
            v = False
        i = i + 1

    return v

def verifierSousGrille(grille, row, col, num):
    '''
            (list, int, int) -> Bool
            Vérifier si la case à ajouter n'existe pas sur la sous-grille.
            Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''

    # A COMPLETER
    v = True
    #Vérifie la sous-grille dans laquelle la position choisie se trouve.
    #n est l'index de ligne du début de la sous-grille.
    #m est l'indice de colonne du début de la sous-grille.
    if row <= 2 and col <= 2:
       n=0
       m=0
    elif row <= 2 and col <= 5:
       n=0
       m=3
    elif row <= 2 and col <= 8:
       n=0
       m=6
    elif row <= 5 and col <= 2:
       n=3
       m=0
    elif row <= 5 and col <= 5:
       n=3
       m=3
    elif row <= 5 and col <= 8:
       n=3
       m=6
    elif row <= 8 and col <= 2:
       n=6
       m=0
    elif row <= 8 and col <= 5:
       n=6
       m=3
    elif row <= 8 and col <= 8:
       n=6
       m=6

    for i in range(n,n+3):
        for j in range (m, m+3):
           if grille[n][m] == num:#Vérifie si le numéro à insérer se trouve dans la sous-grille.
               v= False
        
    return v

           

def verifierGagner(grille):
    
    '''(list) ->  bool
    * Preconditions: grille est une reference a une matrice 9x9 qui contient de nombres de 1 à 9
    * Verifie si la grille est completement remplie.
    '''
    
    # A COMPLETER

    v = True

    i = 0
    while i < len(grille):
        j = 0
        while j < len(grille[i]):
            if grille[i][j] == 0:
                v = False

            j = j + 1

        i = i + 1

    return v




   
  
def verifierValide(grille, row, col, num):
   ''' (list, int, int, int) ->  bool
   * verifie si le nombre proposé est bon sur la ligne et colonne et la sous-grille donné en parametre.
   * Preconditions: tab est une reference a une matrice 9 x 9 qui contient des chiffres entre 1 et 9
   '''
   
   # A COMPLETER


   return (verifierLigne(grille, row, num) and verifierCol(grille, col, num) and verifierSousGrille(grille, row, col, num))
 





   




   
   


