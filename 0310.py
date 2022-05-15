def multa(vV, vM, emer):
    res = None
    vmin = vM / 2
    
    if ( vV <= vM and vV >= vmin ):
        res = "\nNo recibe multa."
        
    elif ( vV >= vM and vV <= (vM * 0.15) + vM ):
        if (emer):
            res = "\nNo recibe multa."
        else:
            res = "\nAdvertencia."
            
    elif ( vV <= vmin and vV >= vmin - (vmin * 0.15) ):
        res = "\nAdvertencia."
        
    elif ( vV > (vM * 0.15) + vM ):
        if (emer):
            res = "\nNo recibe multa."
        else:
            res= "\nRecibe multa por exceso de velocidad."
    
    elif ( vV < vmin - (vmin * 0.15) ):
        res = "\nRecibe multa por entorpecer el tránsito."
    
    return res
    
def main():
    vV = int( input("Velocidad del vehículo: ") )
    vM = int( input("Velocidad máxima: ") )
    emer = input("Emergencia (s/n): ")
    
    if (emer == "S" or emer == "s"):
        emer = True
    else:
        emer = False
        
    print(multa(vV, vM, emer))
    
main()