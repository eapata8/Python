ent = int( input("SVP introduire un entier: "))

if ent%2==0 and ent%3==0 :
  divisiblePar2Par3 = 2
elif ent%2==0 or ent%3==0: 
  divisiblePar2Par3 = 1
else:
  divisiblePar2Par3 = 0
     
if (divisiblePar2Par3 == 0) :
  print("L'entier ", ent, " n'est pas divisible ni par 2 ni par 3")
if(divisiblePar2Par3 == 1): 
  print("L'entier ", ent, " est divisible par 2 ou par 3")
if(divisiblePar2Par3 == 2): 
  print("L'entier ", ent, " est divisible par 2 et par 3")




