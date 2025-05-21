print("kitty patitas suaves")

print("bienvenido a la fundacion kitty patitas suaves, si quiere adoptar una mascota ingrese los siguientes datos")


user=input("ingrese su nombre:")
age=int(input("ingrese su edad:"))
cc= int(input("ingrese su documento:"))
direccion=input("ingrese la direccion de su casa:")
income=int(input("ingrese su sueldo mensual:"))

print("""
      Escoja una de las siguientes opciones:
        1 - Adoptar una mascota
        2 - Dar en adopcion una mascota
        3 - Contactanos
        4 - Salir del programa
""" )

opcion = int(input("ingrese una opcion:"))

while opcion != 4:
    if opcion<1 or opcion>4:
        print("entrada invalida, por favor escoja una opcion entre 1 y 4")
        
        opcion = int(input("\ningrese una opcion:"))
    if opcion == 1:

        def par():

            mascota=input("que mascota quiere (gato o perro):")
            
            if mascota =="gato":
                print("estas son las razas de gatos disponibles: \n siames, persa, siberiano, azul ruso, bombay, exotico\n")
                raza=input("que raza de gato desea?:")
                
                if raza =="siames":
                    print("la raza de gato elegida es siames, estas son las edades disponibles: \n 8 meses, 2 años, 3 años y 4 años\n")
                    años_1=int(input("seleccione la edad del gato siames:"))
                    print("la edad seleccionada para el gato siames es", años_1)

                    print("\n los datos seleccionados son los siguientes:", "\n el tipo de mascota es:", mascota, "\n la raza es:", raza, "\n su edad es:", años_1 )


                if raza =="persa":
                    print("la raza de gato elegida es persa, estas son las edades disponibles: \n 6 meses, 1 años, 3 años y 5 años\n")
                    años_2=int(input("seleccione la edad del gato persa:"))
                    print("la edad seleccionada para el gato persa es", años_2)

                    print("\n los datos seleccionados son los siguientes:", "\n el tipo de mascota es:", mascota, "\n la raza es:", raza, "\n su edad es:", años_2 )

                if raza =="siberiano":
                    print("la raza de gato elegida es siberiano, estas son las edades disponibles: \n 3 meses, 1 años, 2 años y 5 años\n")
                    años_3=int(input("seleccione la edad del gato siberiano:"))
                    print("la edad seleccionada para el gato siberiano es", años_3)

                    print("\n los datos seleccionados son los siguientes:", "\n el tipo de mascota es:", mascota, "\n la raza es:", raza, "\n su edad es:", años_3 )

                if raza =="azul ruso":
                    print("la raza de gato elegida es azul ruso, estas son las edades disponibles: \n 2 meses, 1 años, 4 años y 6 años\n")
                    años_4=int(input("seleccione la edad del gato azul ruso:"))
                    print("la edad seleccionada para el gato azul ruso es", años_4)

                    print("\n los datos seleccionados son los siguientes:", "\n el tipo de mascota es:", mascota, "\n la raza es:", raza, "\n su edad es:", años_4 )

                if raza =="bombay":
                    print("la raza de gato elegida es bombay, estas son las edades disponibles: \n 5 meses, 3 años, 4 años y 7 años\n")
                    años_5=int(input("seleccione la edad del gato siames:"))
                    print("la edad seleccionada para el gato siames es", años_5)

                    print("\n los datos seleccionados son los siguientes:", "\n el tipo de mascota es:", mascota, "\n la raza es:", raza, "\n su edad es:", años_5 )

                if raza =="exotico":
                    print("la raza de gato elegida es exotico, estas son las edades disponibles: \n 4 meses, 2 años, 5 años y 6 años\n")
                    años_6=int(input("seleccione la edad del gato exotico:"))
                    print("la edad seleccionada para el gato exotico es", años_6)

                    print("\n los datos seleccionados son los siguientes:", "\n el tipo de mascota es:", mascota, "\n la raza es:", raza, "\n su edad es:", años_6 )

            if mascota =="perro":
                print("estas son las razas disponibles: \n doberman, pitbull, labrador, husky, criollo, golden retriver\n ")
                
                raza=input("que raza de perro desea?:")
                
                if raza =="doberman":
                    print("la raza de perro elegida es doberman, estas son las edades disponibles: \n 4 meses, 1 año, 3 años y 6 años\n")
                    años_7=int(input("seleccione la edad del perro doberman:"))
                    print("la edad seleccionada para el perro doberman es", años_7)

                    print("\n los datos seleccionados son los siguientes:", "\n el tipo de mascota es:", mascota, "\n la raza es:", raza, "\n su edad es:", años_7 )

                if raza =="pitbull":
                    print("la raza de perro elegida es pitbull, estas son las edades disponibles: \n 4 meses, 1 año, 3 años y 6 años\n")
                    años_8=int(input("seleccione la edad del perro pitbull:"))
                    print("la edad seleccionada para el perro pitbull es", años_8)

                    print("\n los datos seleccionados son los siguientes:", "\n el tipo de mascota es:", mascota, "\n la raza es:", raza, "\n su edad es:", años_8 )

                if raza =="labrador":
                    print("la raza de perro elegida es labrador, estas son las edades disponibles: \n 1 mese, 2 años, 4 años y 5 años\n")
                    años_9=int(input("seleccione la edad del perro labrador:"))
                    print("la edad seleccionada para el perro labrador es", años_9)

                    print("\n los datos seleccionados son los siguientes:", "\n el tipo de mascota es:", mascota, "\n la raza es:", raza, "\n su edad es:", años_9 )

                if raza =="husky":
                    print("la raza de perro elegida es husky, estas son las edades disponibles: \n 6 meses, 2 años, 3 años y 4 años\n")
                    años_10=int(input("seleccione la edad del perro husky:"))
                    print("la edad seleccionada para el perro husky es", años_10)

                    print("\n los datos seleccionados son los siguientes:", "\n el tipo de mascota es:", mascota, "\n la raza es:", raza, "\n su edad es:", años_10 )

                if raza =="criollo":
                    print("la raza de perro elegida es criollo, estas son las edades disponibles: \n 4 meses, 1 año, 2 años y 6 años\n")
                    años_11=int(input("seleccione la edad del perro pitbull:"))
                    print("la edad seleccionada para el perro pitbull es", años_11)

                    print("\n los datos seleccionados son los siguientes:", "\n el tipo de mascota es:", mascota, "\n la raza es:", raza, "\n su edad es:", años_11 )

                if raza =="golden retriver":
                    print("la raza de perro elegida es golden retriver, estas son las edades disponibles: \n 2 meses, 2 años, 3 años y 4 años\n")
                    años_12=int(input("seleccione la edad del perro golden retriver:"))
                    print("la edad seleccionada para el perro golden retriver es", años_12)

                    print("\n los datos seleccionados son los siguientes:", "\n el tipo de mascota es:", mascota, "\n la raza es:", raza, "\n su edad es:", años_12 )
                           

    elif opcion == 2:

        print("ingrese los siguientes datos para dar a adopcion:")

        mascota = input("ingrese el tipo de mascota (perro o gato)")
        raza = input("ingrese la raza de su mascota")
        edad = float(input("ingrese la edad de su mascota"))
    
        print("\n", mascota, "\n", raza, "\n", edad)

    elif opcion == 3:
        
        print("""
              3196810229
              calle 78 cra 11
              """)
    
    else:
        print("\n la opcion ingresada es:", opcion)
        opcion = int(input("\n escoja una opcion:"))

par()

print("fin del programa")
