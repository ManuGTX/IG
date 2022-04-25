def mate(sg, x, y):
    res = None
    
    if (sg == "+"):
        res = x + y
    elif (sg == "-"):
        res = x - y
    elif (sg == "*"):
        res = x * y
    elif (sg == "/"):
        res = x / y
    
    return res

def main():
    x = int( input("Ingrese el primer número: ") )
    y = int( input("Ingrese el segundo número: ") )
    sg = input("Ingrese la operación (+, -, *, /): ")
    
    form = "{} {} {} = {}"
    res = mate(sg, x, y)
    
    print(form.format(x, sg, y, res))
    
main()