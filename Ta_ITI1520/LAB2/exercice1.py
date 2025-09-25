value = input("Entrez une valeur: ")
print("La variable value:", value, 'a un type:', type(value))


#division_entiere = value // 2


value = int(value)
print("Après conversion, value:", value, 'a un type:', type(value))


division_entiere = value // 2
print("division_entiere par 2:", division_entiere)

restant = value % 2
print("restant:", restant)
