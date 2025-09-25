#Auteur : APATA Ruth Esther
#Numéro d'étudiant : 300144673

print("Auteur: APATA Ruth Esther")
print("Numéro d'étudiant : 300144673")

def mesure(monrayon):
    import math
    
    surface = 4*math.pi*(monrayon**2)
    volume = 4*math.pi*(monrayon**3)/3
    print ("La surface de votre sphère est: ", surface)
    print ("Le volume de votre sphère est: ", volume)


mesure(4)



