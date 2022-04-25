def positivismo(real):
    res = None

    if ( real > 0 ):
        res = "positivo"
    
    elif ( real < 0 ):
        res = "negativo"
    
    else:
        res = "cero"

    return res
    
def enterismo(num):
    res = None
    
    if ( (num % 1) == 0 ):
        if ( num > 0 ):
            res = "entero natural"
        else:
            res = "entero"
    else:
        res = "real"
    
    return res
    
def main():
    x = float( input("Ingrese un número: ") )
    form = "El número es {} y {}."
    
    print( form.format( positivismo(x), enterismo(x) ) )
    
    
main()