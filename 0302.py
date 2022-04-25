def orden(x, y, z):
    form = "Los números ordenados en forma ascendente son:\n{}\n{}\n{}"
    
    if (x < y and x < z):
        if (y < z):
            print( form.format(x, y, z) )
        else:
            print( form.format(x, z, y) )
            
    if (y < x and y < z):
        if (x < z):
            print( form.format(y, x, z) )
        else:
            print( form.format(y, z, x) )
        
    if (z < x and z < y):
        if (x < y):
            print( form.format(z, x, y) )
        else:
            print( form.format(z, y, x) )
        
def main():
    x = int (input("Ingrese el primer número: ") )
    y = int( input("Ingrese el segundo número: ") )
    z = int( input("Ingrese el tercer número: ") )
    
    orden(x, y, z)
    
main()
            