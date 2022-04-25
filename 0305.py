def fecha(d, m, a):
    res = None
    
    if ( 12 >= m >= 1 ):
        
        if ( 31 >= d > 0 ):
            
            if ( d == 31 and (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12) ):
                res = True
            
            elif ( d == 30 and m == 2 ):
                res = False
            
            elif ( d == 29 and m == 2 ):
                
                if ( ( a % 4 == 0  and a % 100 != 0 ) or ( a % 400 == 0 ) ):
                    res = True
                
                else:
                    res = False
            
            else:
                res = True
                
        else:
            res = False
    
    else:
        res = False

    return res
    
def main():
    d = int( input("Ingrese el día: ") )
    m = int( input("Ingrese el mes: ") )
    a = int( input("Ingrese el año: ") )
    
    if ( fecha(d ,m, a) ):
        print("\nLa fecha es correcta")
    else:
        print("\nLa fecha es incorrecta")

    
main()