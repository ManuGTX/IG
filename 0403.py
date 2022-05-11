def esPrimo(num):
    i = 2
    primo = True
    while (i < num and primo):
        if (num % i == 0):
            primo = False
        i += 1

    return primo

def rangoPrimos(max):
    print( "\nPrimos entre 1 y {}:".format(max) )
    
    j = 0
    for i in range(1, max):
        if ( esPrimo(i) ):
            j += 1
            if ( j % 10 != 0 ):
                print( "{:4d}".format(i) , end="")
            else:
                print( "{:4d}".format(i) )

def todoPrimos(cant):
    print( "\n\nPrimeros {} primos:".format(cant) )
    
    i = 0
    j = 2 
    while ( i < cant ):
        if ( esPrimo(j) ):
            i += 1
            if ( i % 10 != 0 ):
                print( "{:4d}".format(j) , end="")
            else:
                print( "{:4d}".format(j) )
        j += 1

def main():
    cant = int( input("Ingrese cantidad (numero natural): ") )
    
    rangoPrimos(cant)
    todoPrimos(cant)


main()