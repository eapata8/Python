temp = int( input("Quelle est la temperature? "))

if temp >= 80.0:
  numAct = 1
elif temp >= 60.0 and temp < 80.0: 
  numAct = 2
elif temp >= 40.0 and temp < 60.0: 
  numAct = 3
else: 
  numAct = 4
    
if numAct == 1: 
  print("L'activité recommandée est la natation")
elif numAct == 2: 
  print("L'activité recommandée est le soccer")
elif numAct == 3: 
  print("L'activité recommandée est le volleyball")
elif(numAct == 4):
  print("L'activité recommandée est le ski")




