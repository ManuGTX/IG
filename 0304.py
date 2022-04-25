def check(x, y):
    res = None

    if ( x > y ):
        if ( y <= (x - y) <= x ):
            res = True
        else:
            res = False
    else:
        if ( x <= (y - x) <= y ):
            res = True
        else:
            res = False
    
    return res

def main():
    x = int( input("Ingrese un número A: ") )
    y = int( input("Ingrese un número B: ") )
    
    if ( check(x, y) ):
        print("\nSI cumple condición")
    else:
        print("\nNO cumple condición")
    
main()