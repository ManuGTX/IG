def cargarLstAlu():
    inpt = None
    lst = []
    
    while inpt == None:
        alum = []
        
        alum.append( int(input("DNI:")) )
        alum.append( input("Nombre:") )
        alum.append( int(input("Edad:")) )
        
        lst.append( alum )
        
        if input("Seguir:") == "0":
            inpt = 1
        
    return lst
    
def ordenarAluxDNI(lst):
    lar = len(lst)
    
    for i in range( lar ):
        for j in range( i + 1, lar ):
            if lst[i][0] > lst[j][0]:
                aux = lst[j][0]
                lst[j][0] = lst[i][0]
                lst[i][0] = aux
    
    return lst    
            
def main():
    
    lst = cargarLstAlu()
    print( ordenarAluxDNI(lst) )

main()