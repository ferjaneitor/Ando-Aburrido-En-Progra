import random

CurrencyType = str(input("Ingresa que tipo de taza de cambio buscas, USD o MXN: "))
Currency = float(input("Ingresa la cantidad de dinero que te gustaria cambiar: "))

if CurrencyType == "USD":
    #print(((Currency * 100) / 17)/100)
    if Currency%17 != 0 :
        TotalCurrency = Currency - Currency%17
        print("El dinero total que se te dara es de: ", TotalCurrency/17, " USD")
        print("Pero no se pudo convertir la siguiente cantidad de dinero: ", Currency%17, " MXN")

    else:
        print("El dinero total que se te dara es de: ", Currency/17, " USD")
elif CurrencyType == "MXN":
    print("El dinero total que se te dara es de: ",(Currency * 17), " MXN")
else:
    print("Escribiste algo mal o no aceptamos ese tipo de moneda")

print("")

print("Vamos a jugar a piedra, papel o tijeras")
PlayerMove = str(input("¿Cual es tu jugada?(Todo debe que estar escrito en minusculas): "))

def rockPaperScrisors(PlayerMove):
    ComputerMove = random.choice(['piedra', 'papel', 'tijeras'])

    if PlayerMove == "piedra" and ComputerMove == 'tijeras':
        return "Ganaste, la computadora jugo tijeras y tu piedra"
    elif PlayerMove == "tijeras" and ComputerMove == 'papel':
        return "Ganaste, La computadora jugo papel y tu tijeras"
    elif PlayerMove == "papel" and ComputerMove == 'piedra':
        return "Ganaste, La computadora jugo piedra y tu papel"
    else:
        return "Perdiste, La computadora jugo: " + ComputerMove + " y tu jugaste: " + PlayerMove

print(rockPaperScrisors(PlayerMove))