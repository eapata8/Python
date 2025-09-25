class Personne:
    '''represente une classe Personne'''
    def __init__(self, nom , prenom, identifiant):
        '''(str,str, int)->None
        initialise les attributs de la classe Personne'''
        # A completer
        
        self.nom = nom
        self.prenom = prenom
        self.identifiant = identifiant


    def __repr__(self):
        '''(Personne)->str
        retourne une representation de l'objet'''
        # A completer

        return "La personne " + str(self.nom) + " " + str(self.prenom) + " a pour identifiant " + str(self.identifiant)


        

    def __eq__(self, autre):
        '''(Personne, Personne)->bool
        self == autre si le nom et le prenom sont les memes'''
        # A completer

        return self.nom == autre.nom and self.prenom == autre.prenom and self.identifiant == autre.identifiant



        

class Etudiant(Personne):
    
    '''represente une classe Etudiant'''
     # solde est un attribut de la classe Etudiant
     # cours est une liste de cours (une liste de chaine de caracteres)
     
     # methodes
     
     # A completer

    def __init__(self, nom='', prenom='', identifiant=0, solde=0, cours=[]):
         '''(str,str,int,float,list)-> None
         C'est le constructeur de la classe Etudiant.
         Elle possède les attributs nom, prénom et identifiant hérités de la classe Personne et ses propres attibuts solde et liste de cours.'''

         Personne.__init__(nom, prenom, identifiant)
         self.solde = solde
         self.l_cours = cours

    def __repr__(self):
        ''' (None)-> str
         Retourne comment afficher à l'écran les différents attributs d'un objet de la classe Etudiant.'''

        return "L'étudiant "+str(self.nom)+" "+str(self.prenom)+ " avec l'identifiant "+ str(self.identifiant)+ " a un solde de "+ str(self.solde) + " et les cours" + str(self.l_cours)


    def ajouterCours(self, nomCours):
         '''(str)-> bool
         Retourne True si le cours a été ajouté et False sinon.
         Un cours ne peut-être ajouté que si le solde de l'étudiant est nul.'''
         
         ajout = False

         if self.solde == 0:
             ajout = True
             self.l_cours.append(nomCours)
         else:
             print("Désolé, veuillez régler votre solde.")

         return ajout
             



class Employe(Personne):
    '''represente un employe'''
    # tauxHoraire est un attribut de la classe Employe
    
    # methodes

    # A completer

    def __init__(self, nom='', prenom='', identifiant=0,tauxHoraire=0):
        '''(str,str,int,float)-> None
         C'est le constructeur de la classe Employé.
         Elle possède les attributs nom, prénom et identifiant hérités de la classe Personne et son attibut propre tauxHoraire.'''
        Personne.__init__(nom, prenom, identifiant)
        self.tauxHoraire = tauxHoraire

    def __repr__(self):
        ''' (None)-> str
         Retourne comment afficher à l'écran les différents attributs d'un objet de la classe Employé.'''
        return "L'employé "+ str(self.nom)+ " " + str(self.prenom)+" avec l'identifiant "+ str(self.identifiant)+ " a un taux horaire de "+ str(self.tauxHoraire)

    def calculerSalaire(self, nombreHeure):
        ''' (int)-> float
        Retourne le salaire d'un employé'''
        return nombreHeure * self.tauxHoraire


        


class Gestion:
 listEtudiant = []
 listEmploye = []

 def ajouterEtudiant(self):
    ''' none -> bool
    ajouter des etudiants dans une liste d'etudiant'''
    # Completer

    unEtudiant = Etudiant(input("Quel est le nom de l'étudiant? "),input("Quel est son prénom? "))
    
    while True:
        try:
            unEtudiant.identifiant = int(input("Donnez son identifiant: "))
            break
        except ValueError:
            print ('Essayez des valeurs entières svp')
    while True:
        try:
            unEtudiant.solde = float(input("Quel est l'état de son solde? "))
            break
        except ValueError:
            print ('Essayez des valeurs réelles svp')


    choix = input("Voulez-vous ajouter un cours? ")

    while True:#Se répète autant de fois que le choix est invalide ou affirmatif.
        if choix == "non":
            print("Très bien.")
            break
        elif choix == "oui":
            while choix == "oui":#Pour pouvoir ajouter plusieurs cours.
                cours = input("Donner le nom du cours: ")
                unEtudiant.ajouterCours(cours)
                choix = input("Voulez vous ajouter un cours? ")
        else:
            print("Entrez un choix valide svp, oui ou non.")
            choix = input("Voulez vous ajouter un cours? ")
            
    #La variable ajouté nous permet de savoir si l'étudiant vient tout juste d'être ajouté ou non(parce qu'il existait déjà).    
    ajouté = False
    if unEtudiant in Gestion.listEtudiant:
        print("Etudiant déjà présent.")
    else:
        Gestion.listEtudiant.append(unEtudiant)
        ajouté = True
    return ajouté
    

 def ajouterEmploye(self):
    ''' none -> bool
    ajouter des etudiants dans une liste d'etudiant'''
    # Completer
  

    unEmploye = Employe(input("Quel est le nom de l'employé? "),input("Quel est son prénom? "))

    while True:
        try:
            unEmploye.identifiant = int(input("Donnez son identifiant: "))
            break
        except ValueError:
            print ('Essayez des valeurs entières svp')
    while True:
        try:
            unEmploye.tauxHoraire = float(input("Quel est son taux horaire? "))
            break
        except ValueError:
            print ('Essayez des valeurs réelles svp')

    
    #La variable ajouté nous permet de savoir si l'employé vient tout juste d'être ajouté ou non(parce qu'il existait déjà).
    ajouté = False
    if unEmploye in Gestion.listEmploye:
        print("Employé déjà présent.")

    else:
        Gestion.listEmploye.append(unEmploye)
        ajouté = True
    return ajouté

    
 def SoldeNonPaye(self):
    ''' none -> int
    retourner le nombre des etudiants qui ont un solde non paye'''
    # Completer
    compteur = 0
    for i in Gestion.listEtudiant:
        if i.solde > 0:
            compteur +=1
    return compteur
        
    
 def salaireInd(self,Employe, heures):
    '''(str) -> float
    retourne le salaire d'un employe'''
    # Completer
    if Employe in Gestion.listEmploye:
        salaire = Employe.calculerSalaire(heures)
    else:
        salaire = 0
    return salaire 


#program principal
g = Gestion()
print("Ajoutez des étudiants.")
# Ajouter des etudiants
g.ajouterEtudiant()
g.ajouterEtudiant()

# Ajouter des employes
print("Ajoutez des employés.")
g.ajouterEmploye()
g.ajouterEmploye()
#g.ajouterEmployes()

# Afficher le nombre des employes et des etudiants . L'orthographe tient compte du nombre.
if len(Gestion.listEtudiant) == 1:
    print("il y a: 1 étudiant.")
else:print("il y a: ", len(Gestion.listEtudiant), " étudiants.")

if len(Gestion.listEmploye) == 1:
    print("il y a: 1 employé.")
else:print("il y a: ", len(Gestion.listEmploye), " employés.")

# Afficher le nombre des etudiants qui ont un solde a payer. L'orthographe tient compte du nombre.
if g.SoldeNonPaye() == 1:
    print("il y a 1 étudiant qui n'a pas payé son solde.")
else:
    print("il y a ", g.SoldeNonPaye(), "étudiants qui n'ont pas payé leur solde.")
    
# Afficher les salaires de tous les employes
for e in Gestion.listEmploye:
    while True:
        try:
            heure = int(input("Entrez le nombre d'heures pour l'employé " + e.prenom + " " + e.nom + ": "))
            break
        except ValueError:
            print ('Essayez des valeurs entières svp')
        
    print('Le salaire de:', e.nom, e.prenom, 'est:', g.salaireInd(e,heure), '$.')

#Afficher toute la Gestion
print("Toute la gestion: ")
for i in Gestion.listEtudiant:
    print(i)
for j in Gestion.listEmploye:
    print(j)
