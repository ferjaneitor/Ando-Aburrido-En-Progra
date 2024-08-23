value = int(input("Ingresa un numero: "))

def primo(numero):
    if numero<2:
        return False
    else:
        for i in range(2,numero):
            if numero%i == 0:
                return False
    return True

def ConjeturaDeGoldbach (num):
    if primo(num):
        print("ya es un numero primo", num)
    else:
        for i in range(2, num-1):
            if primo(i):
                b = num - i
                if primo(b):
                    print("Sus primos son: ", i , b)

ConjeturaDeGoldbach(value)