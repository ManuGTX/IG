import math
import random

def azar(x, y):
    ran = random.randint(x, y)
    
    return ran
    
def main():
    x = int( input("Ingrese el limite inferior (numero natural): ") )
    y = int( input("Ingrese el limite superior (numero natural): ") )
    
    uno = azar(x, y)
    dos = azar(uno, y)
    tres = azar(uno, dos)
    
    form = "{}-Limite inferior {}, limite superior {}. Numero generado: {}"
    
    print( form.format(1, x, y, uno) )
    print( form.format(2, uno, y, dos) )
    print( form.format(3, uno, dos, tres) )
    
main()