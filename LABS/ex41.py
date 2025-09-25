def compte(s, c):
   compteur = 0
   index = 0
   while (index < len(s)):
     if (s[index]==c):
        compteur += 1
     index = index + 1
   return compteur

#def compte(s, c):
#   return s.count(c)

s = input("SVP donnez un chaine de caracteres: ")

print(compte(s,'a'))






