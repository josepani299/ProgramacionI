# Inicializacion de las variblaes opcion y salir. Nos permite seleccionar el modo y salir cuando el usuario diga.
import random
def programa():
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
        opcion = int(input("Ingrese una opcion : "))


    # Dentro de cada funcion deberia estar desarrolado su codigo del videojuego/herramienta
    # A su vez cada funcion debera contar con un bucle para permanecer en el juego hasta que el usuario
    # quiera salir al menu principal


        def wordle():
            print("Wordle")

        # Parte de tablas
        def tablas():
            def repaso():
                tablasMultiplicar = []
                for k in range(10):
                    tablasMultiplicar.append([0] * 10)

                for i in range(10):
                    for j in range(10):
                        tablasMultiplicar[i][j] = (i + 1) * (j + 1)

                def mostrartablaespecifica():
                    seguir = True
                    while seguir:
                        tabla = int(input("Ingrese la tabla que quiere repasar: "))
                        tabla -= 1
                        print(f"la tabla {tabla + 1} es: ")
                        for (j) in range(0, 10, 1):
                            print(f"{tabla+1} x {j+1} = ", end=" ")
                            print(tablasMultiplicar[tabla][j])
                        print("\n")
                        salidarepaso = str(input("Quiere repasar otra tabla. Ingrese si/no "))
                        salidarepaso = salidarepaso.lower()
                        if salidarepaso == "si":
                            seguir = True
                        elif salidarepaso == "no":
                            seguir = False
                        else:
                            print("No ingreso una opcion correcta")
                        decision()


                def practicarutablaespecifica():
                    tabla = int(input("Ingrese la tabla para practicar: "))
                    permanecer = True
                    while permanecer:
                        numero = random.randint(1, 10)
                        print(f"Cuanto es: {tabla} x {numero}:")
                        valor = int(input())
                        if valor == tabla * numero:
                            print("Correcto")
                        else:
                            print(f"Incorrecto el valor es {tabla*numero}")
                        permanecer2 = True
                        while permanecer2:
                            opcion = str(input("Quiere seguir jugando, si o no: "))
                            opcion = opcion.lower()
                            if opcion == "si":
                                permanecer2 = False
                                permanecer = True
                            elif opcion == "no":
                                permanecer  = False
                                permanecer2 = False
                                decision()
                            else:
                                print("Ingrese una opcion validad")
                                permanecer2 = True
                print("1- Practicar una tabla especifica")
                print("2- Para mostrar una tabla especifica")
                print("3- Para volver al menu anterior")
                eleccion = int(input())
                if eleccion == 1:
                    practicarutablaespecifica()
                elif eleccion == 2:
                    mostrartablaespecifica()
                elif eleccion == 3:
                    decision()
                else:
                    print("No eligio una opcion correcta")
                    repaso()

            def juego():
                Nombre = str(input("Ingrese su nombre: "))
                salir1 = True
                while salir1:
                    vidas = 3
                    racha = 0
                    while vidas > 0:
                        numerouno = random.randint(1,10)
                        numerodos = random.randint(1,10)
                        print(f"Cuanto es {numerouno} * {numerodos}: ")
                        try:
                            respuesta = int(input())
                            if respuesta == (numerodos * numerouno):
                                racha += 1
                            else:
                                vidas -= 1
                            print(f"Llevas una racha de {racha}")
                            print(f"La cantidad de vida es: {vidas}")
                        except:
                            print("Deberia responder un numero, no se aceptan caracteres")
                    with open("Historial.txt","a") as archivo:
                        archivo.write(Nombre)
                        archivo.write(" ")
                        archivo.write(str(racha))
                        archivo.write("\n")

                    salir2 = True
                    while salir2:
                        volverJugar = str(input("Quiere volver a jugar? Ingrese si o no: "))
                        volverJugar = volverJugar.lower()
                        if volverJugar == "si":
                            salir2 = False
                            juego()
                        elif volverJugar == "no":
                            salir1 = False
                            salir2 = False
                            decision()
                        else:
                            print("Error en respuesta. Solo se reciben  si o no como respuestas")

            def decision():
                print("Bienvenido a ")
                print("╱╭╮╱╱╱╱╱╭╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱")
                print(" ╯╰╮╱╱╱╱┃┃╱╱┃┃╱╱╱╱╱╱╱╱╱╱")
                print("╰╮╭╯╭━━╮┃╰━╮┃┃╱╭━━╮╭━━╮")
                print("╱┃┃╱┃╭╮┃┃╭╮┃┃┃╱┃╭╮┃┃━━┫")
                print("╱┃╰╮┃╭╮┃┃╰╯┃┃╰╮┃╭╮┃┣━━┃")
                print("╱╰━╯╰╯╰╯╰━━╯╰━╯╰╯╰╯╰━━╯")
                print("╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱")
                print("1- Repaso tablas")
                print("2- Practicar tablas")
                print("3- Mostrar la tabla de rachas")
                print(("4- Salir de tablas "))
                try:
                   decisionInicial = int(input("Elija una opcion: "))

                   if decisionInicial == 1:
                            repaso()
                   elif decisionInicial == 2:
                            juego()
                   elif decisionInicial == 3:
                            mostrartabladeracha()
                   elif decisionInicial == 4:
                            programa()
                   else:
                        print("No ingreso una opcion correcta")
                except:
                        print("Recuerde que solo puede ingresar valores numericos")
                        decision()


            def mostrartabladeracha():
                with open("Historial.txt","r", encoding="utf-8") as archivo:
                    linea = archivo.read()
                    print(linea)
                decision()
            decision()
        def Carreras():
            print("Carreras")
        def lenguaje():
            print("Lenguaje")

        # Menu principal

        if opcion == 1:
            wordle()
        elif opcion == 2:
            tablas()
        elif opcion == 3:
            Carreras()
        elif opcion == 4:
            lenguaje()
        elif opcion == 5:
            print("Saliendo... Muchas gracias por jugar")
            break
        else:
            print("No eligio una opcion correcta ")

programa()
