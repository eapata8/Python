def coder(s):
     '''(str)->str
      Retourne un nouveau chaine code
      '''
     s_code=''
     for i in range(0,len(s)-1,2):
          s_code=s_code+s[i+1]+s[i]
     if(len(s)%2==1): # si len(s) est impaire, on ajoute la derniere lettre
          s_code=s_code + s[len(s)-1]
     return s_code



s1 = input("SVP donnez un chaine de caracteres: ")
print(coder(s1))






