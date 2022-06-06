def cortargo(lar, cor):
    num = 0
    i = len(cor)
    j = 0
    while ( i <= len(lar) and cor != "" ):
        if lar[j : i] == cor:
            num += 1
            i = i + len(cor)
            j = i - len(cor)
        else: 
            i += 1
            j += 1

    print(num)
    
def main():
    lar = "Bueno, yo o sea, este ... o sea, o sea"
    cor = ""
    
    cortargo(lar, cor)
    
main()
