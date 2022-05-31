def estaEnLista(num, lst):
    res = None
    if num in lst:
        res = True
    else:
        res = False
    
    return res


def cargarLista():
    print("Ingresar numeros, o 0 (cero) para terminar")
    inpt = int(input())
    lst = []
    
    while ( inpt != 0 ):
        if ( estaEnLista(inpt, lst) ):
            print("Error, numero repetido.")

        elif ( inpt < 0 ):
            print("Error, numero NO positivo.")

        else:
            lst.append(inpt)
        
        inpt = int(input())

    return lst


def main():
    res = cargarLista()
    print("La lista contiene:", res)

main()