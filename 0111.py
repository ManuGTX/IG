num = int( input("Ingrese un nummero decimal (maximo 5 cifras):") )

lista = []

if (num == 0):
    lista.append(0)

while ( num != 0 ):
    lista.append( num % 8 )
    num = num // 8


lista.reverse()

print("Numero en octal: ", end="")
for x in lista:
    print(x, end="")