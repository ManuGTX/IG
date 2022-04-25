def justificado(fra, ancho):
    res = "'{:>{wd}}'".format(fra, wd=(ancho-2))
    return res
    
def main():
    frase = input("Ingrese la frase: ")
    ancho = int( input("Ingrese el ancho total a ser usado: ") )
    
    res = justificado(frase, ancho)
    
    print(res)

main()