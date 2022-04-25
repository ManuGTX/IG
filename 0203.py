import math

def paridad(x):
    
    suma = ((x // 10000000) + ((x // 1000000) % 10) + ((x // 100000) % 10) + ((x // 10000) % 10) + ((x // 1000) % 10) + ((x // 100) % 10) + ((x // 10) % 10) + ((x // 1) % 10))
    
    return suma % 2
        

def main():
    x = int( input("Ingrese un numero binario de hasta 8 bits: ") )
    
    par = paridad(x)
    
    print("Bit de paridad generado: ", par)


main()