def move_zeros_in_place(lst):
     '''lst -> None
        Deplace les zeros de lst a la fin
        en modifiant le contenue de lst
        Precondtion: lst est une liste de nombres
     '''
     front=0;
     back=len(lst)-1
     while(front<back):
          if(lst[front]==0 and lst[back]!=0):
               lst[front]=lst[back]
               lst[back]=0
               front=front+1 
               back=back-1
          elif (lst[front]==0 and lst[back]==0):
               back=back-1
          else:
               front=front+1

x = [1, 0, 3, 0, 0, 5, 7] 
print(x)
move_zeros_in_place(x)
print(x)

