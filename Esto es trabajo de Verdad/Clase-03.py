a=10
b=3

print(a+b) #Suma
print(a-b) #Resta
print(a*b) #Multiplicaicon
print(a/b) #Division
print(a**b) #Exponiente
print(a%b) #Modular o residuo

print(a==b) #igual a
print(a!=b) #no es igual a
print(a>b) #mayor que
print(a<b) #Menor que
print(a>=b) #mayor o igual que
print(a<=b) #menor o igual que

#Cuando es con un solo signo de igual es que estamos asignando valores en un aparte de la memoria
#mientras que cuando usamos 2 signos de igual, estamos comparando que si 2 valores son iguales

def mayorDeEdad (Edad):
    if (Edad>=18):
        print("Ya eres mayor de edad")
    else:
        print("Aun no eres mayor de edad")

edad = int(input("Ingresa tu Edad: "))
mayorDeEdad(edad)

def grading(Calificacion):
    if Calificacion >= 90:
        print("Tu calificacion es de: A")
    elif Calificacion >= 80:
        print("Tucalificacion es de: B")
    elif Calificacion >= 70:
        print("Tu calificacion es de: C")
    else:
        print("Te hace falta repasar")

Calificacion = int(input("Ingresa tu calificacion: "))

grading(Calificacion)