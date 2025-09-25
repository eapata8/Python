def move_zeros_extra_list_no_return(lst):
     '''lst -> None
        Deplace les zeros de lst a la fin
        en utilisant une liste temporaire   
        Precondtion: lst est une liste de nombres
     '''
     tmp=[0]*len(lst) #tmp est remplie avec des zeros
     index_tmp=0
     for i in range(len(lst)):
          if(lst[i]!=0):
               tmp[index_tmp]=lst[i]
               index_tmp=index_tmp+1
    
     # on copy les elements de tmp dans lst
     for i in range (len(lst)):
          lst[i]=tmp[i]

     # notez que sans return on peut pas changer lst directement
     # on peut pas utiliser lst=tmp[:] !!!
     # parce que ca changes la reference lst pas x

x = [1, 0, 3, 0, 0, 5, 7] 
print(x)
move_zeros_extra_list_no_return(x)
print(x)

