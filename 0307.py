def check(x, y, z):
    res = None
    
    if ( ((x >= y and x >= z)   and   (z <= y))   or   ((z >= x and z >= y)   and   (x <= y)) ):
        
        if ( ((x + z)/2) == y ):
            res = True
        
        else:
            res = False
    
    elif ( ((y >= x and y >= z)   and   (z <= x))   or   ((z >= x and z >= y)   and   (y <= x )) ):
        
        if ( ((y + z)/2) == x ):
            res = True
        
        else:
            res = False
    
    else:
        
        if ( ((x + y)/2) == z ):
            res = True
        
        else:
            res = False
    
    return res

def main():
   x = int( input("Ingrese el primer número: ") )
   y = int( input("Ingrese el segundo número: ") )
   z = int( input("Ingrese el tercer número: ") )
   
   res = check(x, y, z)
   
   if ( res ):
       print("\nEstán igualmente distanciados!")
   elif ( not res ):
       print("\nNO están igualmente distanciados!")
    
main()