import random

print("")

print("Hola, vamos a calcular tu indice de Masa, para ello, contesta lo siguiente: ")

Weight = int(input("Ingresa tu peso: "))
Height = int(input("Ingresa tu altura en cm: "))

print("")

def IMC (Peso, Altura):
    Indice = Peso / ((Altura/100) * (Altura/100))
    if( Indice < 18.5):
        print("Estas bajo de peso")
    elif( Indice >= 18.5, Indice <=24.9):
        print("Estas en el peso ideal")
    elif( Indice >= 25, Indice<=29.9):
        print("Tienes sobrepeso")
    else:
        print("Tienes Obesidad")

IMC(Weight,Height)

print("")

print("Vamos a adivinar numeros")

Guess = int(input("Cual numero crees que es?: "))

def RandomGenerator(guess):
    num = random.randint(1,10)

    if(guess < num):
        print("Tu numero es muy pequeño")
    elif( guess > num ):
        print("Tu numero es muy grande")
    else:
        print("Le atinaste")
    
    print("El numero era: ", num)

print("")

RandomGenerator(Guess)