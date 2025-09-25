#Auteurs: Apata Ruth Esther: 300144673
#         Kologo Wendpanga Jean Eliezer:300101810
def triangle(n):
    '''(int)-> None
    Permet d'afficher un triangle rectangle isocèle de longeur n.
    '''
    
    if (n==1):
        print("*", end=(" "))
    else:
        triangle(n-1)#Il faut afficher la ligne des n-1 étoiles avant celle des n étoiles.
        print()
        for i in range(n):
            print("*",end=(" "))


def prodListePos_rec(l,n):
    '''(list,int)->float
       Retourne le produits des nombres strictement positifs de la liste l de longeur n.
    '''
    if n==0:
        p=1
    else:
        if l[n-1]>0:
            p = l[n-1]*prodListePos_rec(l,n-1)
        else: 
            p = prodListePos_rec(l,n-1)
    return p


                         
                         
    
    
