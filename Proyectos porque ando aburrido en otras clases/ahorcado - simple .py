import random

# Lista de palabras
words = ["python", "programacion", "computadora", "juego", "desarrollo"]
# Seleccionar una palabra aleatoria
word = random.choice(words)

# Inicializar la lista para almacenar letras adivinadas
guessed_letters = []

# Bucle para permitir al usuario adivinar letras
while True:
    # Crear una representación actual de la palabra
    updated_wordSpaces = ""
    for letter in word:
        if letter in guessed_letters:
            updated_wordSpaces += f" {letter} "
        else:
            updated_wordSpaces += " __ "

    print("Progreso actual:", updated_wordSpaces)

    # Comprobar si se ha adivinado la palabra
    if all(letter in guessed_letters for letter in word):
        print("¡Felicidades! Has adivinado la palabra:", word)
        break

    guess = input("Adivina una letra: ").lower()

    # Comprobar si la letra ya ha sido adivinada
    if guess in guessed_letters:
        print("Ya adivinaste esa letra. Intenta con otra.")
        continue

    # Añadir la letra a las adivinadas
    guessed_letters.append(guess)

    # Comprobar si la letra está en la palabra
    if guess not in word:
        print("La letra no está en la palabra. Intenta de nuevo.")
