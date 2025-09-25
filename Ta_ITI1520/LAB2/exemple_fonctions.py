"""
 DONNÉES:  
 temp_Fahrenheit

 RÉSULTATS:
 temp_Celsius  

 NOM DE LA FONCTION:
 fahrenheit_en_celsius

 MODULE:
 temp_Celsius <- 5.0 / 9.0 * (temp_Fahrenheit - 32)
 
"""

def fahrenheit_en_celsius(temp_Fahrenheit):
#"Transform la temperature de Farenheit en Celsius"
# temp_celsius est une variable locale, 
# elle existe seulement dans cette fonction

    temp_Celsius = 5.0 / 9.0 * (temp_Fahrenheit - 32)
    return temp_Celsius
# t_fahrenheit et t_celsius sont de variables globales

t_fahrenheit = 212
t_celsius = fahrenheit_en_celsius(t_fahrenheit)

print(t_fahrenheit, "Fahrenheit est", t_celsius,  "Celsius.")
