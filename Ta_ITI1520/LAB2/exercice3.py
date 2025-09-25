"""
 DONNÉES:  
devoirsMoyenne, partiel, examen  
(trois nombres >= zero)
 RÉSULTATS:
 note     
(la note finale)
 EN-TÊTE:
 note <- calcule(devoirsMoyenne,  partiel, examen) 
MODULE:
 note <- devoirsMoyenne*25/100 + partiel*25/100 + 
examen*50/100

"""

def calcule(devoirsMoyenne,  partiel, examen):
    note = devoirsMoyenne*25/100 + partiel*25/100 + examen*50/100
    return note

devoirsMoyenne = int(input(""))
partiel = 80    
examen = 90 
note = calcule(devoirsMoyenne,  partiel, examen)

print("La note finale est:",calcule(devoirsMoyenne,  partiel, examen))
print("La note finale est:",calcule(85,  80, 90))
print("La note finale est:", note)
