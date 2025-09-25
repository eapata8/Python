import math

"""
DONNÉES: coté1, côté2, côté3
RÉSULTATS: S (surface du triangle)

INTERMEDIARES:
EN-TÊTE :
scalculeSurface(Côté1, Côté2, Côté3)

HYPOTHÈSES:
côté1, côté2, côté3 sont des nombres positives
CONTRAINTES:
MODULE:
p← côté1 + côté2 + côté3
s ← sqrt(p* (p - 2*côté 1) * (p - 2* côté2) * (p - 2* côté3)) / 4
- -
"""

from math import sqrt
def calculeSurface(côté1, côté2, côté3):
    p = côté1 + côté2 + côté3
    s = sqrt(p * (p - 2 * côté1) * (p - 2 * côté2) * (p - 2 * côté3)) / 4
    return s

côté1 = 3
côté2 = 4
côté3 = 5
S = calculeSurface(côté1, côté2, côté3)
print("La surface du triangle est:", S)
