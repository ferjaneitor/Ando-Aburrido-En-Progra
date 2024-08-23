Nombre = str(input("¿Como te llamas? "))
edad = int(input("¿Cuantos años tienes? "))
Estudiante = str(input("¿Eres un Estudiante? [Y/N] "))

print("")

print("Tu nombre es: " + Nombre)
print("Tu edad es: " +str(edad))
if( Estudiante == "Y"):
    print("Actualmente eres un estudiante")
elif( Estudiante == "N"):
    print("Actuamente No eres un estudiante")
else:
    print("Favor de solo contestar con uno de las 2 opciones")

print("")

import math

radio = float(input("¿Cual es el radio del circulo que te gustaria calcular su radio? "))

print ("Tu circulo tiene un area de: " + str((radio * radio) * math.pi))

print("")

Numero = float(input("¿Cual es el numero que te gustaria saber si es par o no? "))

def parImpar (numero) :
    if( (numero%2) == 0 ):
        return "Tu numero es Par"
    else:
        return "Tu numero es Impar"

print (parImpar(Numero))