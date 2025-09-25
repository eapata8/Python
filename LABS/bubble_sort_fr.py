def bubbleSort(alist):
    ''' (list)-> None
    Trie une liste 
    '''
    exchanges = True
    NPas = 0
    while exchanges:
       exchanges = False
       for i in range(len(alist)-1):
           NPas += 1
           if alist[i]>alist[i+1]:
               exchanges = True
               alist[i], alist[i+1] = alist[i+1], alist[i]
    print("Nombre de pas", NPas)          

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)
