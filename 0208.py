def crearFila(ancho):
    string = "*" * ancho
    return string
    
def crearRectangulo(ancho, alto):
    rectg = (crearFila(ancho) + "\n") * alto
    return rectg
    
    
def main():
    ancho = int(input('Ingrese ancho: ' ))
    alto = int(input('Ingrese alto: '))
    print( crearRectangulo(ancho, alto) )
    
    
main()