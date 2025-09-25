def move_zeros_with_return(lst):
     '''lst -> lst
        Retourns une nouvelle liste avec les zeros de lst
        a la fin
        Precondtion: lst est une list de nombres
     '''
     tmp=[0]*len(lst) #tmp est remplie avec zeros
     index_tmp=0
     for i in range(len(lst)):
          if(lst[i]!=0):
               tmp[index_tmp]=lst[i]
               index_tmp=index_tmp+1
          
     # on a fini parce que tmp avait deja des zeros
     return tmp

x = [1, 0, 3, 0, 0, 5, 7] 
print(x)
y=move_zeros_with_return(x)
print(x,y)

# si on essaye la suivante x change
# parce que x prends la valeur de la reference a la nouvelle list
x=move_zeros_with_return(x) 
print(x)          
