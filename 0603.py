def cargarConjuntos(lst1, lst2):
    cargarLista(lst1)
    cargarLista(lst2)


def cargarLista(lst):
    print("Ingresar numeros, o 0 (cero) para terminar")
    inpt = int(input())
    
    while ( inpt != 0 ):
        if inpt in lst:
            print("Error, numero repetido.")
        else:
            lst.append(inpt)
        
        inpt = int(input())
    

def union(lst1, lst2):
    res = []
      
    for i in lst1:
        if i not in lst2:
            res.append(i)
            
    for i in lst2:
        if i not in res:
            res.append(i)   
    
    return res

def interseccion(lst1, lst2):
    res = []
    
    for i in lst1:
        if i in lst2:
            res.append(i)
    
    return res
    
def diferencia(lst1, lst2):
    res = [] + lst1
    
    for i in lst1:
        if i in lst2:
            res.remove(i)
    
    return res

def diferenciaSimetrica(lst1, lst2):
    res = []
    
    for i in lst1:
        if i not in lst2:
            res.append(i)
            
    for i in lst2:
        if i not in lst1:
            res.append(i)
    
    return res


def main():
    lst1 = []
    lst2 = []
    opt = None
    
    while ( opt != 6 ):
        print("1. CARGAR CONJUNTOS")
        print("2. UNION")
        print("3. INTERSECCION")
        print("4. DIFERENCIA (A-B)")
        print("5. DIFERENCIA SIMETRICA")
        print("6. SALIR")
    
        opt = int(input("Ingrese el valor de la opción:"))
        
        if opt == 1:
            cargarConjuntos(lst1, lst2)
        elif opt == 2:
            print( union(lst1, lst2) )
        elif opt == 3:
            print( interseccion(lst1, lst2) )
        elif opt == 4:
            print( diferencia(lst1, lst2) )
        elif opt == 5:
            print( diferenciaSimetrica(lst1, lst2) )
        
        
main()