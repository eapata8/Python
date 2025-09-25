def histo_n(t):
   h ={}
   for i in t:
      h[i] = h.get(i,0) + 1
   return h

t = (1,2,-3,3,4,-3,3, 3)
d = histo_n(t)
l1 = list(d.items())
l1.sort()
print(l1)
