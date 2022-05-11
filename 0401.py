def main():
    i = 0
    while( i < 5 ):
        num = int( input("Ingrese numero entero: ") )
        if ( num % 2 == 0 ):
            if ( num % 4 == 0 ):
                print("Numero Par. Tambien es multiplo de 4. Total de numeros pares ingresados:", i)
            else:
                print("Numero Par. Total de numeros pares ingresados:", i)
            i += 1
    
    print("\nFIN")

main()