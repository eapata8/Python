import math
def calculeÉcartType(x):
    m = 0
    for i in x:
      m = m + i
    m = m / len(x)
    s = 0
    for i in x:
      s = s + math.pow((i-m),2)
    écartType = math.sqrt(s/(len(x)-1)); 
    return écartType

ch = input('Veuillez entrer une liste des valeurs separees par virgules: ')
l1 = list(eval(ch))
ecart = calculeÉcartType(l1)
print("L'écart type est:", ecart)
 
