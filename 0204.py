import math

def areaCirc(d):
    area = math.pi * ( math.pow((d/2), 2) )
    
    return area

def areaCuad(l):
    area = l * l
    
    return area
    
def areaNegra(l):
    areaTot = areaCuad(l)
    
    aCircs = ( areaCirc(l / 3) * 2 + areaCirc( l * (2/3) ) )
    
    aNegra = areaTot - aCircs
    
    return aNegra


def main():
    l = int( input("Ingrese el lado: ") )
    
    res = areaNegra(l)
    prc = ( res / areaCuad(l) ) * 100
    
    form = "El area negra es {:.2f} y es un {:.2f}% del area total del cuadrado"
    
    print(form.format(res, prc))

main()