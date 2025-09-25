def vérifieTrié(a, n):
    '''(list, int) -> bool
    Verifie si la liste a est triee. n est la taille de la liste
    '''
    if a[n-2] <= a[n-1] :
       if  n == 2 :
            trié = True
       else:
            trié = vérifieTrié(a, n-1)
    else:
       trié = False

    return trié

