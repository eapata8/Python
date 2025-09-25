class Temps:
  '''classe temporelle'''

  def __init__(self, h=12, m=0, s=0):
    '''(Temps)-> None'''
    self.heure = h
    self.minute = m
    self.seconde = s

  def setTemps(self, h, m=0, s=0):
    '''(Temps)-> None'''        
    self.heure = h 
    self.minute = m
    self.seconde = s

  def affiche_heure(self):
    '''(Temps)-> None'''
    print("{0}:{1}:{2}".format(self.heure, self.minute, self.seconde)) 

  def __repr__(self):
    '''(Temps)-> str'''
    return (str(self.heure) +":" +str(self.minute) +":" +str(self.seconde))

  def __eq__(self, autre):
    '''(Temps)-> bool'''
    return self.heure == autre.heure and self.minute == autre.minute and self.seconde == autre.seconde
  
