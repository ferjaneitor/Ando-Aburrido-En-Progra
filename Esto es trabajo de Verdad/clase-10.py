import random

def main():
    Wins = 0
    Defeat = 0

    while True:
        try:
            print("Hola, vamos a jugar a adivinar el número. Por favor selecciona la dificultad:")
            print("1.- Fácil")
            print("2.- Normal")
            print("3.- Difícil")
            print("4.- Experto")
            print("5.- Legendario")
            print("----------------------------------------------------------------------------------")

            playerDifficulty = int(input("Ingresa aquí el número que corresponda con su dificultad: "))

            if playerDifficulty == 1:
                range_limit = 5
            elif playerDifficulty == 2:
                range_limit = 10
            elif playerDifficulty == 3:
                range_limit = 20
            elif playerDifficulty == 4:
                range_limit = 50
            elif playerDifficulty == 5:
                range_limit = 100
            else:
                print("Dificultad no válida. Intenta de nuevo.")
                continue

            print(f"Escogiste la dificultad de {['Fácil', 'Normal', 'Difícil', 'Experto', 'Legendario'][playerDifficulty - 1]}")
            continue_move = input("¿Deseas continuar con esta dificultad? [Y/N]: ").strip().upper()

            if continue_move == "Y":
                player_move = int(input(f"Adivina el número (entre 1 y {range_limit}): "))
                computer_move = randomMove(range_limit)

                if player_move == computer_move:
                    print(f"¡Ganaste! La computadora seleccionó: {computer_move}, y tú: {player_move}")
                    Wins += 1
                else:
                    print(f"Perdiste. La computadora seleccionó: {computer_move}, y tú: {player_move}")
                    Defeat += 1
                
                print("Has Ganado: ", Wins, " veces, y has perdido: ", Defeat, " veces")
                continue_game = input("¿Te gustaría continuar jugando? [Y/N]: ").strip().upper()
                if continue_game != "Y":
                    print("Gracias por jugar. ¡Hasta luego!")
                    break
            else:
                print("Seleccionaste no continuar. Volviendo a la selección de dificultad.")

        except ValueError:
            print("Escribiste algo que no era un número o no seguiste las reglas. Intenta de nuevo.")

def randomMove(range_limit):
    return random.randint(1, range_limit)

if __name__ == "__main__":
    main()
