# Inicializacion de las variblaes opcion y salir. Nos permite seleccionar el modo y salir cuando el usuario diga.

opcion = 0
salir = 5

# Elecciones para jugar

while opcion != salir:
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
    def Tablas():
        print("Tablas")
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

print("Ahora sí")
