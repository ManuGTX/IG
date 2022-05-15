def perfecto(num):
    res= None
    
    i = 1
    j = 0
    while (i < num):
        if ( num % i == 0 ):
            j += i
        i += 1
    
    if ( j == num and num != 0 ):
        res = True
    else:
        res = False
    
    return res

def main():
    
    print("Primeros 4 números perfectos: ")
    i = 0
    j = 0
    while ( i < 4 ):
        if ( perfecto(j) ):
            print(j)
            i += 1
        j += 1
        
main()