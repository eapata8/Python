class Personne(object):
    def __init__(self, a):
      self.age = a
      self.caracteristique = "rien"
    def __repr__(self): 
      return self.caracteristique + " " + str(self.age)
    
class Magicien(Personne):
    def __init__(self, a):
      Personne.__init__(self,a)  
      self.caracteristique = "chapeau"

class MagicienNoir(Magicien):
    def __init__(self, a):
      Magicien.__init__(self,a)  
      self.couleur = "noir"
      
p1 = Personne(21)
m1 = Magicien(25)
m2 = MagicienNoir(26)

print(p1, m1, m2)
