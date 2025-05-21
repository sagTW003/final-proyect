import time


print("kitty patitas suaves")

time.sleep(1)

print("\nbienvenido a la fundacion kitty patitas suaves, si quiere adoptar o dar a adopcion una mascota ingrese los siguientes datos\n")

time.sleep(1)
user=input("ingrese su nombre:")

time.sleep(1)
age=int(input("ingrese su edad:"))

time.sleep(1)
cc= int(input("ingrese su documento:"))

time.sleep(1)
direccion=input("ingrese la direccion de su casa:")

time.sleep(1)
income=int(input("ingrese su sueldo mensual:"))

time.sleep(1)
print("""
      Escoja una de las siguientes opciones:
        1 - Adoptar una mascota
        2 - Dar en adopcion una mascota
        3 - Contactanos
        4 - Salir del programa
""" )
time.sleep(2)

opcion = int(input("ingrese una opcion:"))

while opcion != 4:
    if opcion<1 or opcion>4:
        time.sleep(1)
        print("entrada invalida, por favor escoja una opcion entre 1 y 4")
        time.sleep(1)
        opcion = int(input("\ningrese una opcion valida:"))
   
    if opcion == 1:

        def par():
            time.sleep(1)
            mascota=input("que mascota quiere (gato o perro):")
            time.sleep(1)
            
            if mascota =="gato":
                time.sleep(1)
                print("estas son las razas de gatos disponibles: \n siames, persa, siberiano, azul ruso, bombay, exotico\n")
                time.sleep(1)
                raza=input("que raza de gato desea?:")
                
                
                if raza =="siames":
                    time.sleep(1)
                    print("la raza de gato elegida es siames, estas son las edades disponibles: \n 8 meses, 2 años, 3 años y 4 años\n")
                    time.sleep(1)
                    años_1=input("seleccione la edad del gato siames:")
                    time.sleep(1)
                    print("la edad seleccionada para el gato siames es", años_1)
                    time.sleep(2)

                    print("\n los datos seleccionados son los siguientes:", "\n el tipo de mascota es:", mascota, "\n la raza es:", raza, "\n su edad es:", años_1 )


                if raza =="persa":
                    time.sleep(1)
                    print("la raza de gato elegida es persa, estas son las edades disponibles: \n 6 meses, 1 años, 3 años y 5 años\n")
                    time.sleep(1)
                    años_2=input("seleccione la edad del gato persa:")
                    time.sleep(1)
                    print("la edad seleccionada para el gato persa es", años_2)
                    time.sleep(2)

                    print("\n los datos seleccionados son los siguientes:", "\n el tipo de mascota es:", mascota, "\n la raza es:", raza, "\n su edad es:", años_2 )

                if raza =="siberiano":
                    time.sleep(1)
                    print("la raza de gato elegida es siberiano, estas son las edades disponibles: \n 3 meses, 1 años, 2 años y 5 años\n")
                    time.sleep(1)
                    años_3=input("seleccione la edad del gato siberiano:")
                    time.sleep(1)
                    print("la edad seleccionada para el gato siberiano es", años_3)
                    time.sleep(2)

                    print("\n los datos seleccionados son los siguientes:", "\n el tipo de mascota es:", mascota, "\n la raza es:", raza, "\n su edad es:", años_3 )

                if raza =="azul ruso":
                    time.sleep(1)
                    print("la raza de gato elegida es azul ruso, estas son las edades disponibles: \n 2 meses, 1 años, 4 años y 6 años\n")
                    time.sleep(1)
                    años_4=input("seleccione la edad del gato azul ruso:")
                    time.sleep(1)
                    print("la edad seleccionada para el gato azul ruso es", años_4)
                    time.sleep(2)

                    print("\n los datos seleccionados son los siguientes:", "\n el tipo de mascota es:", mascota, "\n la raza es:", raza, "\n su edad es:", años_4 )

                if raza =="bombay":
                    time.sleep(1)
                    print("la raza de gato elegida es bombay, estas son las edades disponibles: \n 5 meses, 3 años, 4 años y 7 años\n")
                    time.sleep(1)
                    años_5=input("seleccione la edad del gato siames:")
                    time.sleep(1)
                    print("la edad seleccionada para el gato siames es", años_5)
                    time.sleep(2)

                    print("\n los datos seleccionados son los siguientes:", "\n el tipo de mascota es:", mascota, "\n la raza es:", raza, "\n su edad es:", años_5 )

                if raza =="exotico":
                    time.sleep(1)
                    print("la raza de gato elegida es exotico, estas son las edades disponibles: \n 4 meses, 2 años, 5 años y 6 años\n")
                    time.sleep(1)
                    años_6=input("seleccione la edad del gato exotico:")
                    time.sleep(1)
                    print("la edad seleccionada para el gato exotico es", años_6)
                    time.sleep(2)

                    print("\n los datos seleccionados son los siguientes:", "\n el tipo de mascota es:", mascota, "\n la raza es:", raza, "\n su edad es:", años_6 )

            if mascota =="perro":
                time.sleep(1)
                print("estas son las razas disponibles: \n doberman, pitbull, labrador, husky, criollo, golden retriver\n ")
                time.sleep(1)
                raza=input("que raza de perro desea?:")
                
                if raza =="doberman":
                    time.sleep(1)
                    print("la raza de perro elegida es doberman, estas son las edades disponibles: \n 4 meses, 1 año, 3 años y 6 años\n")
                    time.sleep(1)
                    años_7=input("seleccione la edad del perro doberman:")
                    time.sleep(1)
                    print("la edad seleccionada para el perro doberman es", años_7)
                    time.sleep(2)

                    print("\n los datos seleccionados son los siguientes:", "\n el tipo de mascota es:", mascota, "\n la raza es:", raza, "\n su edad es:", años_7 )

                if raza =="pitbull":
                    time.sleep(1)
                    print("la raza de perro elegida es pitbull, estas son las edades disponibles: \n 4 meses, 1 año, 3 años y 6 años\n")
                    time.sleep(1)
                    años_8=input("seleccione la edad del perro pitbull:")
                    time.sleep(1)
                    print("la edad seleccionada para el perro pitbull es", años_8)
                    time.sleep(2)

                    print("\n los datos seleccionados son los siguientes:", "\n el tipo de mascota es:", mascota, "\n la raza es:", raza, "\n su edad es:", años_8 )

                if raza =="labrador":
                    time.sleep(1)
                    print("la raza de perro elegida es labrador, estas son las edades disponibles: \n 1 mese, 2 años, 4 años y 5 años\n")
                    time.sleep(1)
                    años_9=input("seleccione la edad del perro labrador:")
                    time.sleep(1)
                    print("la edad seleccionada para el perro labrador es", años_9)
                    time.sleep(2)

                    print("\n los datos seleccionados son los siguientes:", "\n el tipo de mascota es:", mascota, "\n la raza es:", raza, "\n su edad es:", años_9 )

                if raza =="husky":
                    time.sleep(1)
                    print("la raza de perro elegida es husky, estas son las edades disponibles: \n 6 meses, 2 años, 3 años y 4 años\n")
                    años_10=input("seleccione la edad del perro husky:")
                    time.sleep(1)
                    print("la edad seleccionada para el perro husky es", años_10)
                    time.sleep(2)

                    print("\n los datos seleccionados son los siguientes:", "\n el tipo de mascota es:", mascota, "\n la raza es:", raza, "\n su edad es:", años_10 )

                if raza =="criollo":
                    time.sleep(1)
                    print("la raza de perro elegida es criollo, estas son las edades disponibles: \n 4 meses, 1 año, 2 años y 6 años\n")
                    time.sleep(1)
                    años_11=input("seleccione la edad del perro pitbull:")
                    time.sleep(1)
                    print("la edad seleccionada para el perro pitbull es", años_11)
                    time.sleep(2)

                    print("\n los datos seleccionados son los siguientes:", "\n el tipo de mascota es:", mascota, "\n la raza es:", raza, "\n su edad es:", años_11 )

                if raza =="golden retriver":
                    time.sleep(1)
                    print("la raza de perro elegida es golden retriver, estas son las edades disponibles: \n 2 meses, 2 años, 3 años y 4 años\n")
                    time.sleep(1)
                    años_12=input("seleccione la edad del perro golden retriver:")
                    time.sleep(1)
                    print("la edad seleccionada para el perro golden retriver es", años_12)
                    time.sleep(2)

                    print("\n los datos seleccionados son los siguientes:", "\n el tipo de mascota es:", mascota, "\n la raza es:", raza, "\n su edad es:", años_12 )
    
    par()
          

    if opcion == 2:
        time.sleep(1)
        print("ingrese los siguientes datos para dar a adopcion:")
        time.sleep(1)
        mascota = input("ingrese el tipo de mascota (perro o gato):")
        time.sleep(1)
        raza = input("ingrese la raza de su mascota:")
        time.sleep(1)
        edad = (input("ingrese la edad de su mascota:"))
        time.sleep(2)
    
        print("\n los datos son:\n", mascota, "\n", raza, "\n", edad)
        time.sleep(2)

        print("""
      Escoja una de las siguientes opciones:
        1 - Adoptar una mascota
        2 - Dar en adopcion una mascota
        3 - Contactanos
        4 - Salir del programa
        """ )
        time.sleep(1)
        opcion = int(input("\n escoja una opcion:"))


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
        """ )
        time.sleep(3)
        opcion = int(input("\n escoja una opcion:"))

   
    else:
        time.sleep(1)
        print("\n la opcion ingresada es:", opcion)
        
        time.sleep(2)

        print("""
      Escoja una de las siguientes opciones:
        1 - Adoptar una mascota
        2 - Dar en adopcion una mascota
        3 - Contactanos
        4 - Salir del programa
        """ )
        time.sleep(2)

        opcion = int(input("\n escoja una opcion:"))


print("fin del programa")


