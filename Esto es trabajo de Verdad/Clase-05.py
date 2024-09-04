contador = 0

def primo(numero):
    if numero<2:
        return False
    else:
        for i in range(2,numero):
            if numero%i == 0:
                return False
    return True

while contador < 100:
    contador +=1
    if (primo(contador)):
        print(contador)

for i in range(0, 11):
    print(" 5 x ",i, " = " , i * 5)