# Jeu de cartes appelé "Pouilleux" 

# L'ordinateur est le donneur des cartes.

# Une carte est une chaine de 2 caractères. 
# Le premier caractère représente une valeur et le deuxième une couleur.
# Les valeurs sont des caractères comme '2','3','4','5','6','7','8','9','10','J','Q','K', et 'A'.
# Les couleurs sont des caractères comme : ♠, ♡, ♣, et ♢.
# On utilise 4 symboles Unicode pour représenter les 4 couleurs: pique, coeur, trèfle et carreau.
# Pour les cartes de 10 on utilise 3 caractères, parce que la valeur '10' utilise deux caractères.

import random

def attend_le_joueur():
    '''()->None
    Pause le programme jusqu'au l'usager appui Enter
    '''
    try:
         input("Appuyez Enter pour continuer. ")
    except SyntaxError:
         pass


def prepare_paquet():
    '''()->list of str
        Retourne une liste des chaines de caractères qui représente tous les cartes,
        sauf le valet noir.
    '''
    paquet=[]
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for val in valeurs:
        for couleur in couleurs:
            paquet.append(val+couleur)
    paquet.remove('J\u2663') # élimine le valet noir (le valet de trèfle)
    return paquet

def melange_paquet(p):
    '''(list of str)->None
       Melange la liste des chaines des caractères qui représente le paquet des cartes    
    '''
    random.shuffle(p)

def donne_cartes(p):
     '''(list of str)-> tuple of (list of str,list of str)

     Retournes deux listes qui représentent les deux mains des cartes.  
     Le donneur donne une carte à l'autre joueur, une à lui-même,
     et ça continue jusqu'à la fin du paquet p.
     '''
     
     donneur=[]
     autre=[]


     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI
     
     for i in range (0,len(p)-1,2):#Donne successivement les cartes à l'humain puis au robot.
         autre.append(p[i])
         donneur.append(p[i+1])
     #Comme le valet de trèfle a été enlevé, le nombre des cartes est impair. Il faut donc donner dernière carte à l'humain.
     autre.append(p[-1])

         
     return (donneur, autre)


def elimine_paires(l):
    '''
     (list of str)->list of str

     Retourne une copy de la liste l avec tous les paires éliminées 
     et mélange les éléments qui restent.

     Test:
     (Notez que l’ordre des éléments dans le résultat pourrait être différent)
     
     >>> elimine_paires(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> elimine_paires(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    resultat=[]


    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI
     
    
    l.sort()#On range d'abord les éléments de la liste l par ordre croissant.
    i=0
    while i < len(l)-1:
        verif = True #Vérif est une variable qui permet de vérifier si l'élément n'a pas de paire dans la liste.
        if (l[i])[0]==(l[i+1])[0]:
            verif = False
            i = i+1#Dans le cas où on trouve une paire, on ne compare pas le dernier élément de la paire avec l'élément suivant de la liste d'où l'incrémentation de l'index.
        if verif == True:
            resultat.append(l[i])#Quand on ne trouve pas une paire,On ajoute le premier élément de la comparaison à la liste resultat.
        i=i+1 #et on va ensuite comparer le deuxième élément de la comparaison avec l'élément suivant de la liste. 
    if verif==True:
        resultat.append(l[-1])#Quand les deux derniers éléments de la liste ne forment pas une paire,il ne faut pas oublier d'ajouter le dernier élément au résultat.             
    random.shuffle(resultat)
    return resultat


def affiche_cartes(p):
    '''
    (list)-None
    Affiche les éléments de la liste p séparées par d'espaces
    '''


    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI
    
    for i in p:
        print(i,end = (" "))
    print("")#Le curseur revient à la ligne.

    

def entrez_position_valide(n):
     '''
     (int)->int
     Retourne un entier du clavier, de 1 à n (1 et n inclus).
     Continue à demander si l'usager entre un entier qui n'est pas dans l'intervalle [1,n]
     
     Précondition: n>=1
     '''

     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI

     x = int(input("SVP entrez un entier de 1 à " + str(n) + ": "))
     while x < 1 or x > n:
         x = int(input("Position invalide. SVP entrez un entier de 1 à " + str(n) + ": "))
     return x
     

def joue():
     '''()->None
     Cette fonction joue le jeu'''
    
     p=prepare_paquet()
     melange_paquet(p)
     tmp=donne_cartes(p)
     donneur=tmp[0]
     humain=tmp[1]

     print("Bonjour. Je m'appelle Robot et je distribue les cartes.")
     print("Votre main est:")
     affiche_cartes(humain)
     print("Ne vous inquiétez pas, je ne peux pas voir vos cartes ni leur ordre.")
     print("Maintenant défaussez toutes les paires de votre main. Je vais le faire moi aussi.")
     attend_le_joueur()
     
     donneur=elimine_paires(donneur)
     humain=elimine_paires(humain)

     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI
    
     while donneur != [] and humain != []:
         print("Votre tour.")
         print("Votre main est:")
         affiche_cartes(humain)
         if len(donneur)>1:
             print("J'ai " + str(len(donneur)) + " cartes. Si 1 est la position de ma première carte et "+ str(len(donneur)) + " la position de ma dernière carte, laquelle de mes cartes voulez-vous? ")
         else:
             print("J'ai " + str(len(donneur)) + " carte. Si 1 est la position de ma première carte et "+ str(len(donneur)) + " la position de ma dernière carte, laquelle de mes cartes voulez-vous? ")
         x = entrez_position_valide(len(donneur))
         if x ==1:
             print("Vous avez demandé ma " + str(x)+"ière carte.")
         else:
             print("Vous avez demandé ma " + str(x)+"ieme carte.")
         print("La voilà. C'est un " + str(donneur[x-1]))
         humain.append(donneur[x-1])
         del(donneur[x-1])
         print("Avec "+ str(humain[-1]) + " ajouté, votre main est: ")
         affiche_cartes(humain)
         humain=elimine_paires(humain)
         print("Après avoir défaussé toutes les paires et mélangé les cartes, votre main est: ")
         affiche_cartes(humain)
         
         attend_le_joueur()
         
         print("Mon tour.")
         y=random.randrange(0,len(humain))#L'ordinateur choisit de manière aléatoire l'index la carte qu'il va prendre à l'humain.
         if y==0:
             print("J'ai pris votre 1ière carte.")
         else:
             print("J'ai pris votre "+ str(y+1)+"ième carte.")
         donneur.append(humain[y])
         del(humain[y])
         donneur=elimine_paires(donneur)

         attend_le_joueur()

     print("J'ai terminé toutes les cartes.")   
     if donneur == []:
         print("Vous avez perdu! Moi, Robot, j'ai gagné.")
     else:
         print("Félicitations! Vous, Humain, vous avez gagné.")
         
# programme principale
joue()

