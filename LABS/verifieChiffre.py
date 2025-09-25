def vérifChiffres( a, n):
    ''' (list, int) -> bool
    a est une liste de taille n
    '''
    if ( n == 0 ):
        tousChiffres = True
    else:    
        if a[n-1] >= 0 and a[n-1] <= 9 :
           tousChiffres = vérifChiffres( a, n-1 )
        else:
            tousChiffres = False
    return tousChiffres 
