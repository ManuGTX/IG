num = float(input("Ingrese numero: "))

pr = int( (num // 10000) )
seg = int( (num // 1000) % 10 )
ter = int( (num // 100) % 10 )
cuar = int( (num // 10) % 10 )
quin = int( (num // 1) % 10 )

print("Separación en dígitos: ", end="")
print(pr**2, seg**2, ter**2, cuar**2, quin**2, sep="-")