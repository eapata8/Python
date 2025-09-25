def celsius_en_fahrenheit(temp_Celsius):
#"Transform la temperature de Celsius en Fahrenheit"
# temp_Fahrenheit est une variable locale, 
# elle existe seulement dans cette fonction 
    temp_Fahrenheit = (9.0 / 5.0 * (temp_Celsius))+ 32
    return temp_Fahrenheit
# t_fahrenheit et t_celsius sont de variables globales



t_celsius = 100
t_fahrenheit = celsius_en_fahrenheit(t_celsius) 
print(t_celsius, "Celsius est", t_fahrenheit,  "Fahrenheit.")

t_celsius = 25
t_fahrenheit = celsius_en_fahrenheit(t_celsius) 
print(t_celsius, "Celsius est", t_fahrenheit,  "Fahrenheit.")