def figurin(wt):
    print()
    for i in range( ((wt//2) + 1) ):
        if i == 0 or i == ((wt/2) + 0.5) - 1:
            jorge = "*" * wt
            print(jorge)
        
        else:
            print("*", end="")
            print(" " * i, end ="")
            print("*" * (wt - ( (i*2) + 2) ), end="")
            print(" " * i, end ="")
            print("*")
            
    
def main():
    wth = int(input("Ingrese ancho:"))
    
    figurin(wth)
    
main()