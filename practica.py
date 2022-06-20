def main():
    x = 17
    
    for i in range((x//2) + 1):
        for j in range(x):
            if i == 0 or i == (x//2) or j == 0 or j == (x - 1):
                print("*", end="")
            elif j >= i + 1 and j < (x - i) - 1 :
                print("*", end="")
            else:
                print(" ", end="")
        print()


main()