def bono(sueldo):
    res = None
    if(sueldo > 2000):
        res = 0.15 * sueldo
    else:
        res = 0.20 * sueldo
    return res
    
def plus(sueldo, hijos, cat):
    res = None
    if (cat >= 7 and cat <= 9):
        res = plusC(sueldo, cat)
    else:
        res = plusC(sueldo, cat) + plusH(sueldo, hijos)
        
    return res
    
def plusH(sueldo, hijos):
    res = None
    if (hijos):
        res = 0.05 * sueldo
    else:
        res = 0
        
    return res
    
def plusC(sueldo, cat):
    res = None
    if (cat >= 1 and cat <= 3):
        res = 0.10 * sueldo
    elif (cat >= 4 and cat <= 6):
        res = 0.12 * sueldo
    elif (cat >= 7 and cat <= 9):
        res = 0.20 * sueldo
        
    return res

def main():
    sueldo = int(input("Sueldo base: "))
    hijos = input("Tiene hijos (s/n)?: ")
    cat = int(input("Ingrese categoría (1-9): "))
    
    if (hijos == "s"):
        hijos = True
    else:
        hijos = False
    
    total = sueldo + bono(sueldo) + plus(sueldo, hijos, cat)
    
    form = "El sueldo total será de ${:.2f}"
    print( form.format(total) )
    
    
main()