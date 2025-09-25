class CompteBancaire(object):
    def __init__(self, nom ='Dupont', solde =1000):
        self.nom, self.solde = nom, solde
         
    def depot(self, somme):
        self.solde = self.solde + somme

    def retrait(self, somme):
        self.solde = self.solde - somme

    def affiche(self):
        print("Le solde du compte bancaire de {} est de {} dollars.".\
              format(self.nom, self.solde))

class CompteEpargne(CompteBancaire):  
    def __init__(self, nom ='Durand', solde =500):
        CompteBancaire.__init__(self, nom, solde)
        self.taux =.3          # taux d'intérêt mensuel par défaut

    def changeTaux(self, taux):
        self.taux =taux

    def capitalisation(self, nombreMois =6):
        print("Capitalisation sur {} mois au taux mensuel de {} %.".\
              format(nombreMois, self.taux))
        for m in range(nombreMois):
            self.solde = self.solde * (100 +self.taux)/100

# Programme de test :
c1 = CompteBancaire('Duchmol', 800)
c1.depot(350)
c1.retrait(200)
c1.affiche()

c2 = CompteEpargne('Duvivier', 600)
c2.depot(350)
c2.affiche()
c2.capitalisation(12)
c2.affiche()
c2.changeTaux(.5)
c2.capitalisation(12)
c2.affiche()
    
