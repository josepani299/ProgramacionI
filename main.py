# Inicializacion de las variblaes opcion y salir. Nos permite seleccionar el modo y salir cuando el usuario diga.
import random

opcion = 0
salir = 5

# Elecciones para jugar

while opcion != salir:
    print("Bienvenido, elige una opcion: ")
    print("1 - Wordle")
    print("2 - Tablas")
    print("3 - Carreras dados")
    print("4 - Lenguaje simbolico")
    print("5 - Salir ")
    opcion =  int(input("Ingrese una opcion : "))


# Dentro de cada funcion deberia estar desarrolado su codigo del videojuego/herramienta
# A su vez cada funcion debera contar con un bucle para permanecer en el juego hasta que el usuario
# quiera salir al menu principal

    def Wordle():
        print("Wordle")



    # Parte de tablas
    def Tablas():

        print("Bienvenido a tablas")
        print("1- Repaso tablas")
        print("2- Practicar tablas")
        decisionInicial = int(input())
        def repaso():
            print("Las tablas son: ")
            tablas = []
            for k in range(10):
                tablas.append([0]*10)

            for i in range(10):
                for j in range(10):
                    tablas[i][j] = (i+1)*(j+1)

            for i in range(10):
                print("\n")
                for j in range(10):
                    print(tablas[i][j], end=" ")
            print("\n")
            Tablas()
        def juego():
            salir = False
            while salir == False :
                vidas = 3
                racha = 0
                while vidas > 0:
                    numerouno = random.randint(1,10)
                    numerodos = random.randint(1,10)
                    print(f"Cuanto es {numerouno} * {numerodos}: ")
                    respuesta = int(input())
                    if respuesta == (numerodos * numerouno):
                        racha += 1
                    else:
                        vidas -= 1
                    print(f"Llevas una racha de {racha}")
                    print(f"La cantidad de vida es: {vidas}")
                decision = str(input("Quiere volver a jugar? Ingrese si o no"))
                decision.lower()
                if decision == "si":
                    salir = False
                elif decision == "no":
                    salir = True
                else:
                    print("Error en respuesta. Solo se reciben  si o no como respuestas")

        if decisionInicial == 1:
            repaso()
        elif decisionInicial == 2:
            juego()
        else:
            print("No ingreso una opcion correcta")

    def Carreras():
        print("Carreras")
    def lenguaje():
        print("Lenguaje")

    if opcion == 1:
        Wordle()
    elif opcion == 2:
        Tablas()
    elif opcion == 3:
        Carreras()
    elif opcion == 4:
        lenguaje()
    elif opcion == 5:
        print("Saliendo... Muchas gracias por jugar")
    else:
        print("No eligio una opcion correcta ")
