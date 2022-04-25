s = int( input("Ingrese tiempo en segundos: ") )

d = ( s / (60*60) ) // 24
h = ( s / (60*60) ) % 24
m = ( s / 60 ) % 60
s = s % 60 

form = "{} dia(s), {} hora(s), {} minuto(s), {} segundo(s)"

print(form.format(int(d), int(h), int(m), int(s)) )