def pgcd(x, y):
        if (x % y == 0):
           res = y
        else: 
           res = pgcd(y, x % y)
        return res
    
