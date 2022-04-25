import math

def raiz(x, n):
    return math.pow(x, 1/n)
    
def main():
    x = int( input("Ingrese el radicando (numero real): ") )
    n = int( input("Ingrese el indice (numero natural): ") )
    
    rz = raiz(x, n)
    form = "\nLa raiz {} de {} es = {:.6f}"
    print(form.format(x, n, rz))

main()