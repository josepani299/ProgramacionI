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
        def Transcriptomania():
            # TRANSCRIPTOMANIA

            print("╔═.✵.═════════════════════════╗")
            print(" BIENVENIDOS A TRANSCRIPTOMANÍA")
            print("╚═════════════════════════.✵.═╝")
            print()

            def introduccion():
                print("Este es un juego diseñado para desafiar tus habilidades de traducción")
                print("entre el lenguaje coloquial y el lenguaje matemático.\n")
                print("Tu misión será interpretar correctamente frases y convertirlas en")
                print("expresiones matemáticas.\n")
                print("¡Es una forma divertida de practicar y aprender!\n")
                print("Lee atentamente cada enunciado, identifica las palabras claves y escribe ")
                print("su equivalente correcto.\n")

                print("¡Demuestra qué tan rápido y preciso puedes ser al resolver cada desafío!\n")
                print("Para asegurarte de que estás preparado, aquí tienes una lista de los ")
                print("símbolos matemáticos básicos que usaremos en el juego:")
                print("Suma: +")
                print("Resta: -")
                print("Multiplicación: *")
                print("División: /")
                print("Potencia: **")
                print("Igualdad: =")
                print("Paréntesis: ()\n")
                print("Recuerda: los paréntesis son importantes para agrupar operaciones ")
                print("y cambiar el orden en que se resuelven las expresiones.\n")
                print("NOTA IMPORTANTE ↓↓↓")
                print("En este juego, utilizaremos la letra x para representar un número cualquiera.")
                print("Por ejemplo:")
                print("→ Un número cualquiera aumentado en dos unidades, se traduciría como x+2")
                print("→ El triple de un número sería 3*x\n")

            def prueba_piloto():
                # Si indica que sí, realizamos la prueba piloto.
                respuestas_practica = 0
                practica_uno = input(" Un número cualquiera: ")
                practica_uno = practica_uno.lower()
                if practica_uno == "x":
                    respuestas_practica += 1
                    print("Su respuesta es correcta.")
                else:
                    print("Su respuesta es incorrecta.")
                practica_dos = input("Un número aumentado en doce unidades: ")
                practica_dos = practica_dos.lower()
                if practica_dos == "x+12":
                    respuestas_practica += 1
                    print("Su respuesta es correcta.")
                else:
                    print("Su respuesta es incorrecta.")
                practica_tres = input("El doble de un número disminuido tres unidades: ")
                practica_tres = practica_tres.lower()
                if practica_tres == "2*(x-3)":
                    respuestas_practica += 1
                    print("Su respuesta es correcta.")
                elif practica_tres == "2*x-3":
                    print("Su respuesta es incorrecta.\n")
                    print("Presta atención a los detalles de la oración:")
                    print("→ Si dice: El doble de un número aumentado en dos unidades")
                    print("la operación correcta es 2*(x+2), porque el número debe ")
                    print("primero ser aumentado en dos unidades antes de duplicarse.\n")
                    print("→ Si la oración tiene una pausa o está separada por una coma, como:")
                    print("El doble de un número, aumentado en dos unidades entonces la ")
                    print("operación es diferente: 2*x+2, ya que primero se duplica el ")
                    print("número y luego se le suman las dos unidades.")
                else:
                    print("Su respuesta es incorrecta.")

                if respuestas_practica == 3:
                    print("\nFELICITACIONES, HAS PASADO LA PRUEBA PILOTO!!")
                    inicio_juego()
                elif respuestas_practica == 2 or 1 or 0:
                    print("\n¡Debes volver a intentarlo!")
                    menu_practica()

            def inicio_juego():
                lenguaje_coloquial = ["1.Jorge tiene el doble de la edad de Manuel. Transcribe la edad de Jorge: ",
                                      "2.La cuarta parte de mi dinero: ",
                                      "3.La edad de mi vecina: ", "4.La mitad de sus ahorros: ",
                                      "5.El cuadrado de un número, aumentado en 5 unidades: ",
                                      "6.El quíntuplo de un número disminuido en 8 unidades: ",
                                      "7.La diferencia de un número y quince es igual a veinte: ",
                                      "8.La suma de un número y su consecutivo es igual a treinta: ",
                                      "9.La diferencia entre dos números pares consecutivos: ",
                                      "10.El doble de un número disminuido en seis unidades es igual a dicho número aumentado en cuatro unidades: ",
                                      "11.La tercera parte de la suma entre un número y su cubo: ",
                                      "12.El triple de la diferencia entre un número y su antecesor: "]
                lenguaje_matematico = {1: "2*x", 2: "x/4", 3: "x", 4: "x/2", 5: "x**2+5", 6: "5*(x-8)", 7: "x-15=20",
                                       8: "x+(x+1)=30", 9: "2x-(2x+1)",
                                       10: "2*(x-6)=x+4", 11: "(x+x**3)/3", 12: "3*(x-(x-1))"}
                puntos = 0
                vidas = 3
                nombre = input("Ingrese su nombre: \n")
                print("¡Prepárate para demostrar tus habilidades!")
                print("¡BUENA SUERTE Y A JUGAR! 🧠🎮")
                jugar = input("Presiona enter para comenzar.\n")
                if jugar == "":
                    print("Comenzamos:")
                    for i in range(0, 12, 1):
                        print(lenguaje_coloquial[i])
                        respuesta = str(input())
                        if respuesta == lenguaje_matematico[i + 1]:
                            print("Su respuesta es correcta.")
                            print(f"La cantidad de vidas que tienes es {vidas}.")
                            puntos += 1
                        else:
                            print("Su respuesta es incorrecta.")
                            vidas -= 1
                            print(f"La cantidad de vidas que tienes es {vidas}.")
                        if vidas <= 0:
                            print("¡Te quedaste sin vidas!")
                            salir_del_juego()
                            break
                        if vidas > 0 and i == 11:
                            print("HAS GANADO. ¡¡FELICIDADES!!")
                            salir_del_juego()
                    with open("resultados.txt", "a") as archivo:
                        archivo.write(nombre)
                        archivo.write("\nNivel alcanzado: ")
                        archivo.write(str(i + 1))
                        archivo.write("\nVidas totales: ")
                        archivo.write(str(vidas))
                        archivo.write("\nPuntaje final: ")
                        archivo.write(str(puntos))

            def menu_practica():
                # Prueba piloto (opcional)
                practica = input("¿QUIERES PRACTICAR? SI/NO \n")  # SI/NO
                practica = practica.upper()
                if practica == "SI":
                    prueba_piloto()
                elif practica == "NO":
                    inicio_juego()
                else:
                    print("No ha ingresado una respuesta correcta.")
                    menu_practica()

            def salir_del_juego():
                jugar = input("¿Quieres salir del juego? SI/NO \n")
                jugar = jugar.upper()
                if jugar == "SI":
                    print("Gracias por jugar a TRANSCIPTOMANÍA. ¡Vuelve pronto!🧠🎮")
                elif jugar == "NO":
                    inicio_juego()
                else:
                    print("No ha ingresado una respuesta correcta.")
                    salir_del_juego()

            introduccion()
            print("PRUEBA PILOTO: Si es la primera vez que vas a jugar, realiza una práctica antes de comenzar!")
            menu_practica()


        # Menu principal

        if opcion == 1:
            wordle()
        elif opcion == 2:
            tablas()
        elif opcion == 3:
            Carreras()
        elif opcion == 4:
            Transcriptomania()
        elif opcion == 5:
            print("Saliendo... Muchas gracias por jugar")
            break
        else:
            print("No eligio una opcion correcta ")

programa()
