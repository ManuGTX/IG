import math

def area(x, y, z):
    p = (x + y + z) / 2
    area = math.sqrt( p*(p-x)*(p-y)*(p-z) )
    return round(area, 2)
    
def main():
    x = int( input("Ingrese lado 1: ") )
    y = int( input("Ingrese lado 2: ") )
    z = int( input("Ingrese lado 3: ") )
    
    res = area(x, y, z)
    print("\nEl area del triangulo es = ", res)

main()