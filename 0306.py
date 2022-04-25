def paridad(x):
    res = None
    
    if ( (x % 2) == 0):
        num = int( input( "Ingrese un número menor que {}: ".format(x) ) )
        
        if ( num < x ):
            res = True
        else:
            res = False
    
    else:
        num = int( input( "Ingrese un número mayor que {}: ".format(x) ) )
        
        if ( num  > x ):
            res = True
        else:
            res = False
            
    return res
    
def main():
    x = int( input("Ingrese un número entero positivo: ") )
    res = paridad(x)
    
    if ( res ):
        print("\nCorrecto!")
    elif ( not res ):
        print("\nIncorrecto!")
        
        
main()