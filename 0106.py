b = int( input("Ingrese base: ") )
a = int( input("Ingrese altura: ") ) 
hip = (a**2 + b**2)**0.5

print("Calculos para un triangulo de base ", b, " y altura ", a, ":", sep="")

form = "<<< Area={:.2f} >>>   <<< Perimetro={:.2f} >>>"

print( form.format( (b*a)/2, b + a + hip ) )
