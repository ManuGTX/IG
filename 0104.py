num = float(input("Ingrese numero: "))

print(num)
print("Parte entera: ", int(num) )
print("Parte fraccionaria: {:.3f}".format(num % 1, 3) )