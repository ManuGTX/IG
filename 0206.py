import math
import random

def azar():
    return random.randint(0, 1)
    
def main():
    x = azar()
    
    unoV = input("Ingrese alternativa 1 para vestimenta: ")
    dosV = input("Ingrese alternativa 2 para vestimenta: ")
    
    unoP = input("Ingrese alternativa 1 para plato: ")
    dosP = input("Ingrese alternativa 2 para plato: ")
    
    unoB = input("Ingrese alternativa 1 para bebida: ")
    dosB = input("Ingrese alternativa 2 para bebida: ")
    
    form = "Cena al azar: {}, {} y {}"
    
    print( form.format() )

main()