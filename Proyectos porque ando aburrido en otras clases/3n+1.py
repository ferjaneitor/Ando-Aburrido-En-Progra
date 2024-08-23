Valor = int(input("Ingresa un Numero: "))

def consejuturaDeCollats (num):
    while num > 1 :
        if ((num%2) == 0):
            num = num/2
            print(str(num))
        else:
            num *=3
            num +=1
            print(str(num))

consejuturaDeCollats(Valor)