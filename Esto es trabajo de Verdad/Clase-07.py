CollectData = True
Grades = []
SignatureNumber = 1

while CollectData:
    # El usuario ingresa la calificacion que obtuvo
    SingleGrade = int(input(f"Ingresa la calificación de tu materia número {SignatureNumber}: "))
    
    # Se agrega a la lista la calificacion
    Grades.append(SingleGrade)
    
    # Le preguntamos que si quiere continuar
    CollectDataContinue = input("¿Te gustaría ingresar la calificación de otra materia? [Y/N]: ").strip().upper()
    
    # Si no quiere continuar, interrumpimos el bucle
    if CollectDataContinue == "N":
        CollectData = False
    else:
        # Incrementamos el numero del a materia ingresada dpor uno
        SignatureNumber += 1

# Imprimimos las califaicaciones guardadas
print("Las calificaciones ingresadas son:", Grades)

#Funcion para sacar el promedio
def Avarage(Grades):
    if len(Grades) > 0:
        return sum(Grades)/len(Grades)

if len(Grades) > 0 :

    print("Este es tu promedio: ", Avarage(Grades))

    if Avarage(Grades) >= 70 :
        print("Felicidades!, pasaste el curso podras pasar al siguiente semestre")
    else:
        print("Lo siento mucho pero reprobaste, debes que esforzarte mas")
else:
    print("No ingresaste las calificaciones de manera adecuada")