def espaces(s):
   '''(str)->str
      Retourne une nouvelle chaine avec des espaces
   '''
   index = 0
   nS = ""
   while (index < len(s)):
     nS = nS + s[index] + ' '
     index = index + 1
   nS=nS.strip()
   return nS

def espaces_v1(s):
     '''(str)->str
      Retourne une nouvelle chaine avec des espaces
      '''
     s_emph=''
     for char in s:
          s_emph=s_emph+char+' '
     s_emph=s_emph[0:len(s_emph)-1]
     return s_emph

#s = input("SVP donner un chaine de caracteres: ")
#print(espaces(s),"--", sep='')
#print(espaces_v1(s),"--", sep='')




