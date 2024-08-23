# nombre = "ana"
# Edad = 25

# print("Hola "+ nombre + "Nada mas para confirmar me gustaria saber si tu edad son " + str(Edad) + " años no?") 

# int = 24
# str = "WaSAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.............!!!"
# float = 3.1416
# bool = True

# print(type(int))
# print(type(str))
# print(type(float))
# print(type(bool))

# yo = [["Fernando Joel Cruz Briones", 16, True],
#       ["Keyla Aisha Cox Parales", 17, True],
#       ["Juan Andres Martines Palacios", 16, False],
#       ["Jose Francisco Vargas Zaragoza", 16, False]]

# for i in yo:
#     print("")
#     print("Hola me llamo "+str(i[0])),
#     print("Actualmente tengo " +str(i[1])),
#     if(i[2] == True):
#         print("A mi si me gusta Programar")
#     else:
#         print("A mi no me gusta Programar")
#     print("")


#     #Este apartado es para el algoritmo para hacer un sandwich

# Ingredientes=[
#     "Pan Integral de Molde",
#     [
#         "Mayoneza",
#         "Mostaza",
#     ],
#     [
#         "Jamon de Pavo",
#         "Lechuga",
#         "Jitomate Cherry",
#         "Lonchas de Queso",
#     ],
# ]

# print("")

# def HacerUnSandwich(Ingridients):
#     Sandwich =[]
#     if(Ingridients[0] != "Pan Integral de Molde"):
#         print("Corta el pan a la mitad")
#     print("poner a dorar tus rebanadas de pan")
#     print("Agarras una renabanada ya dorada de pan en un plato")
#     Sandwich.append("Pan Integral de Molde")
#     for I in Ingridients[1]:
#         print("Unta un poquito de: " +str(I))
#         Sandwich.append(I)
#     print("Lo siguiente es")
#     for I in Ingridients[2]:
#         print("Agrega: "+I)
#         Sandwich.append(I)
#     print("Agarra la otra rebanada de pan y")
#     for I in Ingridients[1]:
#         print("Unta un poquito de: " +str(I))
#         Sandwich.append(I)
#     print("Para despues ponerlo ensima de todo lo que previamente has armado")
#     Sandwich.append("Pan Integral de Molde")
#     print("ya si gustas puedes cortarlo a la mitad y a disfrutar, ya terminaste de hacer tu sandwich, ahora la estructura de tu sandwich deberia que parecerse al siguiente: "+str(Sandwich))

# HacerUnSandwich(Ingredientes)

Nombre="Fernando Joel Cruz Briones"
Edad= 16
Progra= True

print("Hola me llamo "+Nombre+" Actualmente tengo " + str(Edad) + " y mi gusto por la programacion es " +str(Progra))