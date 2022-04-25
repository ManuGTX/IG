num = input("Ingrese numero de cantidad impar de cifras (al menos 3 cifras): ")
can = len(num)
num = int(num)

print("El numero ingresado tiene", can, "cifras.")

cen = ( num // (10 ** (can // 2)) ) % 10
ult = num % 10
pri = num // (10 ** (can - 1) )

form = "La primera cifra es {}, la ultima es {} y la central es {}."
print(form.format(pri, ult, cen))
