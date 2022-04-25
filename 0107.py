x = int(input("Ingrese el primer numero: "))
y = int(input("Ingrese el segundo numero: "))

u = x % 10
d = ((y // 10) % 10) * 10


print("El numero resultante es: ", u + d)