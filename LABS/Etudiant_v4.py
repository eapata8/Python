class Etudiant(object):
    ''' Un etudiant a un numero d'etudiant, une note pour l'examen partiel,
        une note pour l'examen final, et une valeur boolene 
    '''
    poidsDevoirs = 0.25
    poidsPartiel = 0.20
    poidsFinal = 0.55

    def __init__(self, num, examPartiel =0, examFinal =0, créditable =True ):
      self.numEtud = num
      self.examPartiel = examPartiel
      self.examFinal = examFinal
      self.créditable = créditable
      self.devoirs=[0,0,0,0,0]
        
    def calculeNoteFinale(self):
      return Etudiant.poidsPartiel * self.examPartiel + \
             Etudiant.poidsFinal * self.examFinal + \
             Etudiant.poidsDevoirs * self.calculeMoyDevoirs()

    def calculeMoyDevoirs(self):
      res = 0
      for val in self.devoirs:
        res = res + val
      return res / len(self.devoirs)

    def affiche(self):
      print("Numero d'etudiant", self.numEtud)
      print("Examen partiel", self.examPartiel)
      print("Examen final", self.examFinal)
      print("Creditable", self.créditable)
      print()

Etudiant.poidsPartiel = 0.25
Etudiant.poidsPartiel = 0.50

unEtudiant = Etudiant(1234567, 60, 80)  # création d'un objet
unEtudiant.affiche()
unEtudiant.devoirs[0] = 100
unEtudiant.devoirs[1] = 90
unEtudiant.devoirs[2] = 95
unEtudiant.devoirs[3] = 87
unEtudiant.devoirs[4] = 100
print("Note finale:", unEtudiant.calculeNoteFinale())
print()

moiAussi = Etudiant(1069665, 73, 79, False)  # création d'un autre objet
moiAussi.affiche()
moiAussi.devoirs[0]=100
moiAussi.devoirs[1]=67
print("Note finale:", moiAussi.calculeNoteFinale())

