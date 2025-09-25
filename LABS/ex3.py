import math

def calculeDistances (v):
    dist = []
    g = 9.8                     # Constante:  gravité 
    degÀRad = math.pi / 180.0   # Constante:  degrés -> radians
    nbrAngles = 10              # Constante: nombres d'angles    
    thêta = 0
    while  thêta <= 90 :
      thêtaRad = degÀRad * thêta
      dist.append(2.0 * v * v * math.cos(thêtaRad) * math.sin(thêtaRad) / g)
      thêta = thêta + 10
    return dist

vitesse = float(input('S.V.P. donnez la vitesse (m/s): '))
distances = calculeDistances(vitesse)
index = 0
while index < len(distances): 
      thêta = index * 10
      print("Pour l'angle",thêta," degrés, la balle parcourt",distances[index]," metres")
      index +=1
      
