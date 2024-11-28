import random

def guardar_partida(nombre, resultado, palabra_secreta, intentos_restantes, letras_incorrectas):
    with open("partidas_jugadas.txt", "a") as vararchivo:
        vararchivo.write("Jugador: " + nombre + "\n")
        vararchivo.write("Resultado: " + resultado + "\n")
        vararchivo.write("Palabra secreta: " + palabra_secreta + "\n")
        vararchivo.write("Intentos restantes: " + str(intentos_restantes) + "\n")
        vararchivo.write("Letras incorrectas: " + ", ".join(letras_incorrectas) + "\n")
        vararchivo.write("...................................\n") 

#Comienza el juego
def jugar_wordle():

    print("............................................")
    print("HOLAAAAA!!!!                               .")
    print("")
    print("BIENVENID@ A WORDLE                        .")
    print("")
    print("UN JUEGO PARA ADIVINAR UNA PALABRA AL AZAR .")
    print("............................................")

    nombre = input("¿COMO ES TU NOMBRE?: ").capitalize()
    print("")
    ganador = False

    lista_palabras = ["flores", "jazmin", "clavel", "lirios", "tigres", "leones", "jirafa", "delfin", "hierba", "viento", 
                    "trueno", "niebla", "aurora", "pulmon", "higado", "vejiga", "brazos", "pierna", "cuello", "hombro", 
                    "olfato", "parque", "puente", "tienda", "medico", "pintor", "libros", "sillas", "puerta", 
                    "pastas", "pollos", "sarten", "platos"]

    tablero = []
    palabra_secreta = random.choice(lista_palabras).upper()
    longitud_palabra = len(palabra_secreta)

    # Inicializa el tablero
    # Crea un tablero vacío de 6 filas
    for i in range(6):  
        fila = ["_"] * longitud_palabra  # Crea una fila con guiones bajos
        tablero.append(fila)  # Añade la fila al tablero

    contador = 0
    letras_incorrectas = []  # Lista para almacenar letras incorrectas


    def es_palabra_valida(texto):
        # Verifica que no sean solo letras repetidas (AAA...)
        if texto == texto[0] * len(texto):
            return False
        return True

    # Bucle principal del juego
    while not ganador and contador < 6:
        print("Tienes", 6 - contador, "intentos para adivinar la palabra.")
        print("")
        print("ingresa una palabra de 6 letras ejemplo: leonel")
        print("")
        texto = input("Introduce una palabra: ").upper()
        print("......................................................................")
        print("Las letras correctas en posicion CORRECTAS se muestran en Mayusculas")
        print("")
        print("Las letras correctas en posicion INCORRECTAS se muestran en minusculas")
        print("......................................................................")

        # En caso de que no se ingrese nada 
        if texto == "":
            print("¡ERROR! No ingresaste ninguna palabra.")
            continue  # Vuelve a pedir la palabra sin continuar el resto del código

        # Verifica longitud y validez de la palabra
        while len(texto) != longitud_palabra or not es_palabra_valida(texto):
            if len(texto) != longitud_palabra:
                print("La palabra debe tener", longitud_palabra, "caracteres.")
            else:
                print("ERROR: La palabra no debe tener todas las letras iguales.")
            texto = input("Introduce una palabra: ").upper()

        # Procesa si la palabra es correcta
        if palabra_secreta == texto:  # Verifica si la palabra ingresada es correcta

            # Si la palabra es correcta, actualiza el tablero con esa palabra
            fila_correcta = []  
            for letra in texto:
                fila_correcta.append(letra)  # Agrega cada letra a la fila
            tablero[contador] = fila_correcta  # Coloca la fila en el tablero
            
            ganador = True  # Marca que el jugador ha ganado

        else:
            # Verifica letras correctas/incorrectas
            intento = []
            palabra_temporal = list(palabra_secreta)  # Copia temporal de la palabra secreta para controlar duplicados

            # Primero verifica letras correctas en la posición correcta
            for i in range(longitud_palabra):
                if texto[i] == palabra_temporal[i]:
                    intento.append(texto[i])  # Letra correcta en posición correcta (mayúscula)
                    palabra_temporal[i] = "_"  # Marca la posición como usada
                else:
                    intento.append("_")  # Por ahora, asume que es incorrecta

            # Luego verifica letras correctas en posición incorrecta
            for i in range(longitud_palabra):
                if texto[i] != palabra_secreta[i] and texto[i] in palabra_temporal:
                    intento[i] = texto[i].lower()  # Letra correcta en posición incorrecta (minúscula)
                    palabra_temporal[palabra_temporal.index(texto[i])] = "_"  # Marca la letra como usada

                elif texto[i] != palabra_secreta[i] and intento[i] == "_":
                    # Letra incorrecta, añadir a la lista de incorrectas si no está ya
                    if texto[i] not in letras_incorrectas:
                        letras_incorrectas.append(texto[i])

            tablero[contador] = intento  # Actualiza el tablero con el intento


        # Muestra la fila como una cadena de texto
        for fila in tablero:
            fila_como_texto = " ".join(fila)
            print(fila_como_texto)

        # Muestra las letras incorrectas
        print("Letras incorrectas o repetidas utilizadas:", ", ".join(letras_incorrectas))
        
        contador += 1  # Incrementa el contador de intentos

    # Mensaje final si gana o pierde el juegador
    if ganador:
        print("¡FELICITACIONES,", nombre, "! DESCUBRISTE LA PALABRA Y GANASTE EL JUEGO.")
        guardar_partida(nombre, "Ganó", palabra_secreta, 6 - contador, letras_incorrectas)
    else:
        print("LO SIENTO,", nombre.upper() + ". PERDISTE. LA PALABRA ERA", palabra_secreta + ".")
        guardar_partida(nombre.upper(), "Perdió", palabra_secreta, 6 - contador, letras_incorrectas) 

# Bucle para jugar de nuevo
while True:
    jugar_wordle()
    jugar_nuevamente = input("¿Quieres jugar otra partida? (si/no): ").lower()
    if jugar_nuevamente != "si":
        print("Espero hayas disfrutado del juego, gracias por jugar.")
        break