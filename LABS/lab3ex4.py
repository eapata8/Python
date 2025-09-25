import math
print("Donnez les trois coefficients.")
a = int(input())
b = int(input())
c = int(input())

#print(a,b,c)

discriminant = math.pow(b,2) - 4*a*c
if discriminant < 0.0 :
  nbrR = 0
elif discriminant > 0.0 :
  nbrR = 2
else: 
  nbrR = 1

print (nbrR)      
