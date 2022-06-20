from random import randint

def esL(let):
    if (let >= "a" and let <= "z") or (let >= "A" and let <= "Z"):
        res = True
    else:
        res = False
    
    return res

def pal(fra):
    pals = 0
    lar = len(fra)
    j = 0
    i = 0

    while i < lar:
        if esL(fra[i]):
            j = i
            esLetra = True
            
            while ( esLetra ):
                if not esL(fra[j]):
                    pals += 1
                    esLetra = False
                    i = j
                
                elif j == lar - 1:
                    pals += 1
                    esLetra = False
                    i = lar
                
                else:
                    j += 1
        else:
            i += 1 

    return pals

def max(fra):
    pala = ""
    lar = len(fra)
    j = 0
    i = 0

    while i < lar:
        if esL(fra[i]):
            j = i
            esLetra = True
            
            while ( esLetra ):
                if not esL(fra[j]):
                    if len(fra[i:j]) > len(pala):
                        pala = fra[i:j]
                    
                    esLetra = False
                    i = j
                
                elif j == lar - 1:
                    if len(fra[i:]) > len(pala):
                        pala = fra[i:]
                    
                    esLetra = False
                    i = lar
                
                else:
                    j += 1
        else:
            i += 1 
            

    return pala

def min(fra):
    pala = ""
    lar = len(fra)
    j = 0
    i = 0

    while i < lar:
        if esL(fra[i]):
            j = i
            esLetra = True
            
            while ( esLetra ):
                if not esL(fra[j]):
                    if len(fra[i:j]) < len(pala) or pala == "":
                        pala = fra[i:j]
                    
                    esLetra = False
                    i = j
                
                elif j == lar - 1:
                    if len(fra[i:]) < len(pala) or pala == "":
                        pala = fra[i:]
                    
                    esLetra = False
                    i = lar
                
                else:
                    j += 1
        else:
            i += 1 
            

    return pala

def main():
    stri = "Palabras {}, may {} y min {}"
    fra = "Si hay problema serio, la nave vuelve a la base"


    print(stri.format( pal(fra), max(fra), min(fra)))
    # print( max(fra) )

main()