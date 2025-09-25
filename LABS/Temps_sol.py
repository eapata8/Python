class Temps:
  '''classe temporelle'''

  def __init__(self, h=12, m=0, s=0):
    '''(Temps)-> None'''
    self.heure = h
    self.minute = m
    self.seconde = s
    self.setTemps(h,m,s)

  def setTemps(self, h, m=0, s=0):
    '''(Temps)-> None'''
    if ( s > 59 ):
           m = m + s // 60  # trouver le nombre des minutes à ajouter
           s = s % 60      # remettre les secondes à l’intervalle [0,59]
    if ( m > 59 ):
           h = h + m // 60  # trouver le nombre d’heures à ajouter
           m = m % 60       # remettre les minutes à l’intervalle [0,59]
           
    self.heure = h % 24   # remettre les heures à l’intervalle [0,23]
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

  def estAvant(self, t2):
     '''(Temps) -> bool 
     retourne True si le temps représenté par self est avant le temps de t2,
     et False sinon'''
     avant =  self.heure < t2.heure or (self.heure == t2.heure and self.minute < t2.minute) or (self.heure == t2.heure and self.minute == t2.minute and self.seconde < t2.seconde)
     return avant

  def durée(self, t2):
     ''' (Temps) -> Temps
     retourne un nouvel objet Temps avec le nombre d’heures, de minutes,
     et de secondes entre self et t2'''
     if self.estAvant(t2):
         diffS = 60*60*(t2.heure - self.heure) + 60*(t2.minute - self.minute) + (t2.seconde - self.seconde)
     else: 
         diffS = 60*60*(self.heure - t2.heure) + 60*(self.minute - t2.minute) + (self.seconde - t2.seconde)
     résultat = Temps()
     résultat.setTemps(0, 0, diffS) # Calculera le nombre d'heures
     return résultat
