def nombreDeChiffres(n):
        print( "1: Entrant la fonction avec n  =", n )
        
        resteDeChiffres = n // 10
        if (resteDeChiffres == 0):
            print("5: Cas de base avec n =", n )
            compteur = 1
        else:
            print("2: Appel récursif venant de n =", n )
            compteur = nombreDeChiffres( resteDeChiffres )
            print("3: Revenant d'un appel récursif avec n =", n )
            compteur = compteur + 1
        
        print( "4: Revenant de la fonction avec n =", n, ", compteur =", compteur )
        return compteur


print(nombreDeChiffres(45612))
