#Auteur: Apata Ruth Esther
#Numéro d'étudiant: 300144673
print("Auteur: Apata Ruth Esther")
print("Numéro d'étudiant: 300144673")

def sequenceDesDeux(a):
    '''
     (list)-> bool

     Retourne True s’il y a au moins une séquence de deux éléments consécutifs égaux, et False dans le cas contraire.
    '''
    
    i=0
    result = False
    while i<len(a) - 1 and result==False:#La boucle s'arrête dès qu'on trouve deux éléments consécutifs égaux.
        if a[i] == a[i+1]:
            result = True
        i = i + 1
    return result

liste = input("Veuillez entrer une liste des entiers par des virgules: ")
a = list(eval(liste))
print(sequenceDesDeux(a))
    
