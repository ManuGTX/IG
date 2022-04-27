def esPrimo(num):
    i = 2
    primo = True
    while (i < num and primo):
        if (num % i == 0):
            primo = False
        i += 1

    return primo

def main():
    x = int( input("Numero: ") )
    print( esPrimo(x) )

main()