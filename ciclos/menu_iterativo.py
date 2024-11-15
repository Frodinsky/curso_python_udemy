print("***Sistema de administracion de cuentas***")

salir = False

while not salir:
    print(f"""Menu:
    1. Crear Cuenta: 
    2. Borrar Cuenta: 
    3. Salir: """)

    opcion = int(input("Digite una opcion"))

    if opcion == 1:
        print("Cuenta creada\n")
    elif opcion == 2:
        print("Cuenta borrada\n")
    elif opcion == 3:
        print("Saliendo del menu\n")
        salir = True
    else:
        print("Opcion invalida")
