def promedio(n1, n2, n3):
    return ( (n1 + n2 + n3) / 3 )
    
def recprom(n1, n2, n3, rec):
    return ( (n1 + n2 + n3 + rec) / 4 )

def situacion(n1, n2, n3):
    pro = promedio(n1, n2, n3)
    notas = ( n1 >= 4 and n2 >= 4 and n3 >= 4 )
    
    if ( notas   and   ( pro >= 7 ) ):
        print( "Promedio general = {:.2f}".format( pro ) )
        print("El alumno ha aprobado la materia.")

    elif ( notas   and   ( pro < 7 ) ):
        print( "Promedio general = {:.2f}".format( pro ) )
        print("El alumno deberá rendir exámen final.")
        
    elif ( not notas ):
        rec = int( input("Ingrese la nota del recuperatorio: ") )
        nwpro = recprom(n1, n2, n3, rec)
        
        if ( rec >= 4 ):
            print( "Promedio general = {:.1f}".format( nwpro ) )
            print("El alumno deberá rendir exámen final.")
        else:
            print( "Promedio general = {:.1f}".format( nwpro ) )
            print("El alumno ha reprobado la materia.")
        
def main():
    n1 = int( input("Ingrese la nota del primer parcial: ") )
    n2 = int( input("Ingrese la nota del segundo parcial: ") )
    n3 = int( input("Ingrese la nota del tercer parcial: ") )
    
    situacion(n1, n2, n3)
    
main()