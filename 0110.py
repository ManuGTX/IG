num = int(input("Ingrese un numero binario: "))

pr = (num // 10000)
seg = (num // 1000) % 10 
ter = (num // 100) % 10 
cuar = (num // 10) % 10 
quin = (num // 1) % 10 

sum = pr * 2 ** 4 + seg * 2 ** 3 + ter * 2 ** 2 + cuar * 2 ** 1 + quin * 2 ** 0 

print("Numero en decimal:", sum)