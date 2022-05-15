def mensaje(uno, cinco, mtot):
    res = None
    
    stock = (uno * 1) + (cinco * 5)
    
    if (stock < mtot):
        res = "No es posible cubrir el tendido."
    else:
        if (mtot // 5 <= cinco and (mtot % 5) != 0 and (mtot % 5) <= uno):
            res = "si, con {}5m y {}1m".format(mtot // 5, mtot % 5)
        elif (mtot // 5 <= cinco and mtot % 5 == 0):
            res = "si, con {}5m".format(mtot // 5)
        elif (mtot <= uno and mtot % 1 == 0):
            res = "si, con {}1m".format(mtot)
        else:
            res = "No"
    
    return res
    
def main():
    uno = int(input("Cantidad de caños de 1 metro: "))
    cinco = int(input("Cantidad de caños de 5 metros: "))
    mtot = int(input("Metros totales a cubrir: "))
    

    print(mensaje(uno, cinco, mtot))
    
main()