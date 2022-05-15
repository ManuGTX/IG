def cond(num):
    res = None
    
    uniCent = (num % 10) + ((num//100) % 10)
    decMil = ((num//10) % 10) + ((num//1000) % 10)
    
    if ( uniCent == decMil ):
        res = True
    
    return res
    
def main():
    for i in range(1000, 10000):
        if ( cond(i) ):
            print(i)

main()