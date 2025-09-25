def initListe(L, n):
    if n != 0:
      initListe( L, n-1 )        
      L.append(n-1)

n = int(input("SVP entrez n: "))
L = []
initListe(L, n)
print(L)
