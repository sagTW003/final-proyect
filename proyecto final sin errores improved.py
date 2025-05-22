import time
import random

def input_numerico(mensaje):
    entrada = input(mensaje)
    while not entrada.isdigit():
        print("Entrada invalida. Por favor ingrese un valor numerico valido.")
        entrada = input(mensaje)
    return int(entrada)

def generar_edades(tipo):
    if tipo == "gato":
        return random.sample(["1 mes", "2 meses", "3 meses", "4 meses", "6 meses", "7 meses", "8 meses", "1 año"], 4)
    elif tipo == "perro":
        return random.sample(["2 meses", "4 meses", "6 meses", "8 meses", "9 meses", "1 año", "1 año y medio", "2 años"], 4)

def par():
    time.sleep(1)
    mascota = input("que mascota quiere (gato o perro):").lower()
    while mascota not in ["gato", "perro"]:
        print("Entrada invalida. Por favor ingrese 'gato' o 'perro'.")
        mascota = input("que mascota quiere (gato o perro):").lower()
    time.sleep(1)

    if mascota =="gato":
        time.sleep(1)
        print("estas son las razas de gatos disponibles: \n siames, persa, siberiano, azul ruso, bombay, exotico\n")
        time.sleep(1)
        raza = input("que raza de gato desea?:").lower()

        while raza not in ["siames", "persa", "siberiano", "azul ruso", "bombay", "exotico"]:
            print("Raza invalida. Ingrese una raza de la lista disponible.")
            raza = input("que raza de gato desea?:").lower()
        time.sleep(1)

        edades_disponibles = generar_edades("gato")
        print("estas son las edades de gatos disponibles: \n", ", ".join(edades_disponibles), "\n")
        time.sleep(1)
        edad = input("seleccione la edad del gato {}: ".format(raza))

        while edad not in edades_disponibles:
            print("edad invalida. Ingrese una edad de la lista disponible.")
            edad = input("que edad desea?:").lower()

        time.sleep(1)
        print("\n los datos seleccionados son los siguientes:\n tipo de mascota:", mascota, "\n raza:", raza, "\n edad:", edad)

    if mascota =="perro":
        time.sleep(1)
        print("estas son las razas disponibles: \n doberman, pitbull, labrador, husky, criollo, golden retriver\n")
        time.sleep(1)
        raza = input("que raza de perro desea?:").lower()

        while raza not in ["doberman", "pitbull", "labrador", "husky", "criollo", "golden retriver"]:
            print("Raza invalida. Ingrese una raza de la lista disponible.")
            raza = input("que raza de perro desea?:").lower()
        time.sleep(1)

        edades_disponibles = generar_edades("perro")
        print("estas son las edades de perros disponibles: \n", ", ".join(edades_disponibles), "\n")
        time.sleep(1)
        edad = input("seleccione la edad del perro {}: ".format(raza))

        while edad not in edades_disponibles:
            print("edad invalida. Ingrese una edad de la lista disponible.")
            edad = input("que edad desea?:").lower()

        time.sleep(1)
        print("\n los datos seleccionados son los siguientes:\n tipo de mascota:", mascota, "\n raza:", raza, "\n edad:", edad)

print("kitty patitas suaves")

time.sleep(1)
print("\nbienvenido a la fundacion kitty patitas suaves, si quiere adoptar o dar en adopcion una mascota ingrese los siguientes datos\n")

time.sleep(1)
user = input("ingrese su nombre:")

time.sleep(1)
age = input_numerico("ingrese su edad:")

time.sleep(1)
cc = input_numerico("ingrese su documento:")

time.sleep(1)
direccion = input("ingrese la direccion de su casa:")

time.sleep(1)
income = input_numerico("ingrese su sueldo mensual:")

time.sleep(1)
print("""
      Escoja una de las siguientes opciones:
        1 - Adoptar una mascota
        2 - Dar en adopcion una mascota
        3 - Contactanos
        4 - Salir del programa
""")
time.sleep(2)

opcion = input_numerico("ingrese una opcion:")

while opcion != 4:
    if opcion < 1 or opcion > 4:
        time.sleep(1)
        print("entrada invalida, por favor escoja una opcion entre 1 y 4")
        time.sleep(1)
        opcion = input_numerico("\ningrese una opcion valida:")

    if opcion == 1:
        par()

    elif opcion == 2:
        time.sleep(1)
        print("ingrese los siguientes datos para dar a adopcion:")
        time.sleep(1)
        mascota = input("ingrese el tipo de mascota (perro o gato):").lower()
        while mascota not in ["perro", "gato"]:
            print("Tipo de mascota invalido. Ingrese 'perro' o 'gato'.")
            mascota = input("ingrese el tipo de mascota (perro o gato):").lower()
        time.sleep(1)
        raza = input("ingrese la raza de su mascota:")
        time.sleep(1)
        edad = input("ingrese la edad de su mascota:")
        time.sleep(2)
        print("\n los datos son:\n", mascota, "\n", raza, "\n", edad)
        time.sleep(2)

    elif opcion == 3:
        time.sleep(2)
        print("""
              telefono: 3196810229
              Ubicacion: calle 78 cra 11 Universidad EAN
              """)
        time.sleep(2)

    print("""
    Escoja una de las siguientes opciones:
        1 - Adoptar una mascota
        2 - Dar en adopcion una mascota
        3 - Contactanos
        4 - Salir del programa
    """)
    time.sleep(2)
    opcion = input_numerico("\n escoja una opcion:")

print("fin del programa")
