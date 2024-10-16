import random
import time
from os import system

#Constantes
MAX_TRIES = [10, 8, 6, 4]
DIFFICULTY_LABELS = ["Fácil", "Normal", "Difícil", "Leyenda"]

#Diccionario de palabras
diccionare = [
    [ #Facil
        {"name": "esperanza", "definition": "Confianza en que algo deseado suceda."},
        {"name": "silencio", "definition": "Ausencia de ruido."},
        {"name": "cultura", "definition": "Conjunto de conocimientos y creencias compartidos."},
        {"name": "sabiduria", "definition": "Conocimiento profundo y reflexivo."},
        {"name": "historia", "definition": "Relato de acontecimientos pasados."},
        {"name": "libertad", "definition": "Estado de no estar sometido."},
        {"name": "honor", "definition": "Valor moral que implica respeto."},
        {"name": "verdad", "definition": "Conformidad de lo que se dice con la realidad."},
        {"name": "conocimiento", "definition": "Información adquirida o entendimiento."},
        {"name": "empatia", "definition": "Capacidad de comprender los sentimientos de otros."},
        {"name": "justicia", "definition": "Principio moral que busca la equidad."},
        {"name": "identidad", "definition": "Conjunto de características que definen a una persona."},
        {"name": "solidaridad", "definition": "Apoyo mutuo entre individuos."},
        {"name": "compasion", "definition": "Sentimiento de empatía hacia el sufrimiento ajeno."},
        {"name": "lealtad", "definition": "Fidelidad a una persona o causa."},
        {"name": "tolerancia", "definition": "Aceptación de ideas o prácticas diferentes."},
        {"name": "responsabilidad", "definition": "Compromiso de asumir las consecuencias de las acciones."},
        {"name": "coherencia", "definition": "Conformidad y consistencia entre ideas y acciones."},
        {"name": "generosidad", "definition": "Disposición a dar y compartir recursos."},
        {"name": "optimismo", "definition": "Actitud positiva ante la vida."},
    ],
    [ #Normal
        {"name": "interaccion", "definition": "Acción que ocurre entre dos o más elementos."},
        {"name": "nostalgia", "definition": "Sentimiento de tristeza por el pasado."},
        {"name": "comunicacion", "definition": "Proceso de intercambio de información."},
        {"name": "resiliencia", "definition": "Capacidad de adaptarse a situaciones adversas."},
        {"name": "identidad", "definition": "Características que definen a un individuo o grupo."},
        {"name": "justicia", "definition": "Principio moral que busca la equidad y el respeto."},
        {"name": "perspectiva", "definition": "Punto de vista desde el cual se observa algo."},
        {"name": "influencia", "definition": "Capacidad de afectar o cambiar a otros."},
        {"name": "transformacion", "definition": "Cambio significativo en la forma o naturaleza de algo."},
        {"name": "sabiduria", "definition": "Conocimiento compartido."},
        {"name": "creatividad", "definition": "Capacidad de generar ideas originales."},
        {"name": "sostenibilidad", "definition": "Capacidad de mantener un equilibrio en los recursos."},
        {"name": "diversidad", "definition": "Variedad de elementos dentro de un grupo."},
        {"name": "autenticidad", "definition": "Veracidad y originalidad en las acciones."},
        {"name": "compromiso", "definition": "Obligación de cumplir con una causa o propósito."},
        {"name": "colaboracion", "definition": "Trabajo conjunto para lograr un objetivo."},
        {"name": "innovación", "definition": "Introducción de ideas o métodos nuevos."},
        {"name": "desarrollo", "definition": "Progreso y mejora en un contexto determinado."},
        {"name": "empoderamiento", "definition": "Proceso de aumentar la confianza en uno mismo."},
        {"name": "conexión", "definition": "Relación que se establece entre dos o más elementos."},
    ],
    [ #Dificil
        {"name": "conexion", "definition": "Relación que permite la interacción entre elementos."},
        {"name": "paradoja", "definition": "Situación que presenta contradicciones evidentes."},
        {"name": "epistemologia", "definition": "Estudio del conocimiento y su naturaleza."},
        {"name": "utopia", "definition": "Sociedad ideal que representa un estado de perfección."},
        {"name": "cognicion", "definition": "Proceso mental de adquisición de conocimiento."},
        {"name": "axiologia", "definition": "Estudio de los valores y su influencia."},
        {"name": "antropocentrismo", "definition": "Perspectiva que considera al ser humano como centro."},
        {"name": "dialectica", "definition": "Método de argumentación que busca la verdad."},
        {"name": "existencialismo", "definition": "Filosofía que enfatiza la libertad individual."},
        {"name": "interseccionalidad", "definition": "Análisis de cómo diferentes opresiones se cruzan."},
        {"name": "neurociencia", "definition": "Estudio del sistema nervioso y el cerebro."},
        {"name": "sociologia", "definition": "Estudio de las sociedades y sus interacciones."},
        {"name": "psicologia", "definition": "Estudio del comportamiento humano y los procesos mentales."},
        {"name": "filosofía", "definition": "Reflexión crítica sobre la existencia y el conocimiento."},
        {"name": "metafisica", "definition": "Estudio de la naturaleza de la realidad."},
        {"name": "teoría del caos", "definition": "Estudio de sistemas complejos e impredecibles."},
        {"name": "cibernetica", "definition": "Estudio de sistemas automáticos y su control."},
        {"name": "semiotica", "definition": "Estudio de los signos y su significado."},
        {"name": "metacognicion", "definition": "Reflexión sobre los propios procesos de pensamiento."},
        {"name": "fenomenologia", "definition": "Estudio de la experiencia y la conciencia."},
    ],
    [ #Leyenda
        {"name": "multiculturalismo", "definition": "Reconocimiento de diversas culturas en una sociedad."},
        {"name": "metacognicion", "definition": "Reflexión sobre los propios procesos mentales."},
        {"name": "ontologia", "definition": "Estudio del ser y de la existencia."},
        {"name": "hermeneutica", "definition": "Teoría de la interpretación de textos."},
        {"name": "deconstruccion", "definition": "Método crítico que busca analizar conceptos."},
        {"name": "teoría del caos", "definition": "Estudio de sistemas complejos e impredecibles."},
        {"name": "sociopolitica", "definition": "Análisis de las relaciones entre sociedad y política."},
        {"name": "ciberespacio", "definition": "Entorno virtual creado por la interconexión digital."},
        {"name": "sostenibilidad", "definition": "Capacidad de mantener el equilibrio en los recursos."},
        {"name": "paradigma", "definition": "Modelo o conjunto de creencias que guía el pensamiento."},
        {"name": "epistemología crítica", "definition": "Estudio crítico de la naturaleza del conocimiento."},
        {"name": "biopoder", "definition": "Control sobre la vida y los cuerpos."},
        {"name": "posmodernismo", "definition": "Corriente cultural y filosófica que cuestiona las narrativas."},
        {"name": "cosmopolitismo", "definition": "Ideología que promueve la unidad global."},
        {"name": "neocolonialismo", "definition": "Dominación indirecta de una nación sobre otra."},
        {"name": "ciberfeminismo", "definition": "Feminismo en el contexto digital."},
        {"name": "transhumanismo", "definition": "Movimento por la evolución del ser humano."},
        {"name": "postestructuralismo", "definition": "Rechazo de estructuras fijas en el análisis."},
        {"name": "bioetica", "definition": "Ética en las ciencias biológicas y médicas."},
        {"name": "antropologia", "definition": "Estudio de la humanidad y sus culturas."},
    ]
]

#Funcion para seleccionar una palabra random
def SelectRandomWord(DiccionareIndex):
    return random.choice(diccionare[DiccionareIndex])

#Funcion para dibujar en la consola el monito y este ira cambiando dependiendo que tantos intentos lleves por lo mismo @Intput : Tries , MaxTries, WordSpaces @return : dibujo
#Esto es de esta forma puesto que el mono tiene 4 disitntos estados en el que se encuentra dibujado por lo que compararemos cuantos intentos llevas y cuales osn los intentos maximos
#Lo que es la funcion @var : WordSpaces lo que nos sirve es para imrpimir en el dibujo las casillas de cuantas letras tienen nuestra palabra y cuantas adiviniaste
def DrawHangMan (tries, MaxTries, WordSpaces) :
    print("________________________________________________________________________________________________")
    print("|                                                                                              |")
    print("|   |___________________________________________________________________________________________")
    print("|   |                                                                                   |    |")
    print("|   |                                                                                   |    |")
    print("|   |                                                                                   |    |")

    if tries <=MaxTries-6:
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
    elif tries == MaxTries-5:
        print("|   |                                                                                    ____")
        print("|   |                                                                                  /      \\")
        print("|   |                                                                                 |        |")
        print("|   |                                                                                 \\        /")
        print("|   |                                                                                    ____")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
    elif tries == MaxTries-4:
        print("|   |                                                                                    ____")
        print("|   |                                                                                  /      \\")
        print("|   |                                                                                 |        |")
        print("|   |                                                                                 \\        /")
        print("|   |                                                                                    ____")
        print("|   |                                                                                     ||")
        print("|   |                                                                                   ______")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
    elif tries == MaxTries-3:
        print("|   |                                                                                    ____")
        print("|   |                                                                                  /      \\")
        print("|   |                                                                                 |        |")
        print("|   |                                                                                 \\        /")
        print("|   |                                                                                    ____")
        print("|   |                                                                                     ||")
        print("|   |                                                                                   ______")
        print("|   |                                                                                  / /  ")
        print("|   |                                                                                 / / ||")
        print("|   |                                                                                / /  ||")
        print("|   |                                                                               / /   ||")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
    elif tries == MaxTries-2:
        print("|   |                                                                                    ____")
        print("|   |                                                                                  /      \\")
        print("|   |                                                                                 |        |")
        print("|   |                                                                                 \\        /")
        print("|   |                                                                                    ____")
        print("|   |                                                                                     ||")
        print("|   |                                                                                   ______")
        print("|   |                                                                                  / /  \\ \\")
        print("|   |                                                                                 / / || \\ \\")
        print("|   |                                                                                / /  ||  \\ \\")
        print("|   |                                                                               / /   ||   \\ \\")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
        print("|   |")
    elif tries == MaxTries-1:
        print("|   |                                                                                    ____")
        print("|   |                                                                                  /      \\")
        print("|   |                                                                                 |        |")
        print("|   |                                                                                 \\        /")
        print("|   |                                                                                    ____")
        print("|   |                                                                                     ||")
        print("|   |                                                                                   ______")
        print("|   |                                                                                  / /  \\ \\")
        print("|   |                                                                                 / / || \\ \\")
        print("|   |                                                                                / /  ||  \\ \\")
        print("|   |                                                                               / /   ||   \\ \\")
        print("|   |                                                                                     ||")
        print("|   |                                                                                     ||")
        print("|   |                                                                                    ----")
        print("|   |                                                                                   //")
        print("|   |                                                                                  //")
        print("|   |                                                                                 // ")
    elif tries == MaxTries:
        print("|   |                                                                                    ____")
        print("|   |                                                                                  /      \\")
        print("|   |                                                                                 |        |")
        print("|   |                                                                                 \\        /")
        print("|   |                                                                                    ____")
        print("|   |                                                                                     ||")
        print("|   |                                                                                   ______")
        print("|   |                                                                                  / /  \\ \\")
        print("|   |                                                                                 / / || \\ \\")
        print("|   |                                                                                / /  ||  \\ \\")
        print("|   |                                                                               / /   ||   \\ \\")
        print("|   |                                                                                     ||")
        print("|   |                                                                                     ||")
        print("|   |                                                                                    ----")
        print("|   |                                                                                   //  \\\\")
        print("|   |                                                                                  //    \\\\")
        print("|   |                                                                                 //      \\\\")

    print("|   |")
    print("|   |")
    print("|   |     ", WordSpaces)

#Esta es una funcion para conseguir el input de nuestro jugador y como en la dificultad facil ya viene por defecto la pista por lo mismo se cambiara el mensaje de la consola
#Tambien lo que nos interesa es que el input se convierta a minusculas y despues eliminar los espacios
def get_player_input(difficulty):
    if difficulty == 1:
        return input("Ingresa una letra para jugar: ").lower().strip()
    else:
        player_input = input("Ingresa una letra o 'pista' para jugar: ").lower()
        return player_input.strip()

#Es una funcion para actualizar el estatus que tenemos con el juego, siendo este cuantos intentos llevamos, las palabaras que tenemos, intentos restantes y letras adivinadas
def display_game_status(word, guessed_letters, tries, max_tries):
    word_spaces = " ".join([letter if letter in guessed_letters else "__" for letter in word])
    DrawHangMan(tries, max_tries, word_spaces)
    print(f"Intentos restantes: {max_tries - tries}")
    print(f"Letras adivinadas: {' '.join(sorted(guessed_letters))}")

#Esta es la funcion donde tenemos toda la logica del juego
def play_game(difficulty):

    #Creamos nuestras constantes y variables del juego
    max_tries = MAX_TRIES[difficulty - 1]
    tries = 0
    guessed_letters = set()
    
    selected_word = SelectRandomWord(difficulty - 1)
    word = selected_word["name"]
    definition = selected_word["definition"]

    #Ya empezamos a jugar al juego y siempre sera esto siempre y cuando los intentos sean menor que los intentos maximo, primero vamos a limpiar la consola
    #Despues empezaremos actualizando el estatus a como este hasta el momento
    #Llamamos @funtion : get_player_input(dificulty)
    #Empezamos a comparar y vemos que hay 2 arboles, cuando la longitud de la palabra  no es igual a 1 y cuando es igual a 1
    #Cuando vemos que la longitud no es igual a 1 son palabras largas por lo que supondremos que el jugador o querra saber una pista o querra adivinar la palabra completa
    #Cuando vemos que la longitud es igual a 1 supondremos que el jugador querra adivinar alguna letra de la palabra
    while tries < max_tries:
        system("cls")
        display_game_status(word, guessed_letters, tries, max_tries)

        if difficulty == 1:
            print("Pista:", definition)

        player_input = get_player_input(difficulty)

        if player_input == "pista":
            print("Pista:", definition)
            time.sleep(5)
            continue
        
        if len(player_input) != 1:
            if player_input == word:
                print(f"¡Felicidades! Has adivinado la palabra: {word}")
                return
            else:
                print("Incorrecto. ¡Intenta de nuevo!")
                tries += 1
                time.sleep(2)
                continue

        if len(player_input) == 1 :
            if player_input in guessed_letters:
                print("Ya has adivinado esa letra.")
                time.sleep(2)
                continue

            if player_input not in word:
                tries += 1
                print("Incorrecto. ¡Intenta de nuevo!")
                time.sleep(2)

            guessed_letters.add(player_input)

        if all(letter in guessed_letters for letter in word):
            print(f"¡Felicidades! Has adivinado la palabra: {word}")
            return

    print(f"Perdiste. La palabra era: {word}")

system("cls")

#Esta es nuestra @funtion : Main
#Esta contendra en su totalidad la implementacion de todo lo anterior por lo que empezaremos con un bucle preguntando la dificultad que querra nuestro jugador
#Esto nos sirve para llamar @funtion : play_game para de esta forma empezar el juego 
#Cuando termine todo esto lo que hara es preguntarle al jugador si va a querer continuar jugando para termine los bucles o continuar
def Main():
    system("cls")
    continue_playing = True

    while continue_playing:
        try:
            print("Selecciona tu dificultad")
            for i, label in enumerate(DIFFICULTY_LABELS, 1):
                print(f"{i}. {label}")
            difficulty = int(input("Ingresa aquí tu dificultad: "))
            if 1 <= difficulty <= 4:
                play_game(difficulty)
            else:
                print("Dificultad no válida")
        except ValueError:
            print("Ingresaste un valor no válido")

        continue_playing_input = input("¿Te gustaría continuar jugando? (y/n): ").lower()
        continue_playing = continue_playing_input == "y"

Main()