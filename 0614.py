def agregarDicEle2(dico):
    inpt = 0
    
    while inpt != None:
        key = int(input("Clave (número): "))
        es = input("Español: ")
        en = input("Inglés: ")
        pt = input("Portugês: ")
        
        dico[key] = (es, en , pt)
        
        if input("Seguir: ") == "no":
            inpt = None
    
    return dico

def main():
    dico = {}
    agregarDicEle2(dico)
    num = 0
    inpt = 0
    
    while inpt != None:
        inpt = int( input("Ingresar número a traducir o cero para salir: ") )
        
        if inpt == 0:
            inpt = None
        elif inpt not in dico:
            print("ERROR: ", end="")
        else:
            num = inpt
            inpt = None
            
    inpt = 0
    
    while inpt != None:
        inpt = input("Ingresar idioma ['es', 'en', 'pt']: ")
        
        if inpt == 0:
            inpt = None
        elif inpt != "es" and inpt != "en" and inpt != "pt":
            print("ERROR: ", end="")
        else:
            if inpt == "es": idi = 0
            elif inpt == "en": idi = 1
            elif inpt == "pt": idi = 3
            
            print( "\n{} en {}: {}".format(num, inpt, dico[num][idi]) )
        
main()