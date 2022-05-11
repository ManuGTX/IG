def maxMin():
    esCero = False
    mayor = None
    menor = None

    input("Ingrese numeros enteros positivos (finalice con 0): ")
    
    while( not esCero ):
        num = int(input())
        if( num == 0 ):
            esCero = True
        elif( mayor == None or num > mayor ):
            mayor = num
        elif( menor == None or num < menor ):
            menor = num

    return "El mayor es {} y el menor es {}.".format(mayor, menor)

def main():
    res = maxMin()
    
    print(res)


main()