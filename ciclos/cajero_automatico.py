print("***Este programa es un cajero automatico***")

SALDO_INICIAL = 1000
terminar = False


while not terminar:
    print("""Opciones que puedes realizar
    1. Depositar
    2. Reitrar
    3. Ver saldo
    4. Salir
    """)
    eleccion = int(input("Digite la opcion que quiere tomar: "))
    #ingresos =
    #retiro =

    if eleccion == 1:
        ingresos = int(input("Cuanto quiere depositar? "))
        print(f"Se ha depositado con exito {ingresos}")
        SALDO_INICIAL += ingresos
    elif eleccion == 2:
        retiro = int(input("Cuanto desea retirar? "))
        #VALIDACION
        if retiro < SALDO_INICIAL:
            print(f"Tu nuevo saldo es ${SALDO_INICIAL}")
        else:
            print("No puedes retirar mas de lo que tines")

    elif eleccion == 3:
        print(f"Tu saldo es ${SALDO_INICIAL}")

    elif eleccion == 4:
        print("Saliendo del cajero automatico :) ")
        terminar = True
    else:
        print("Opcion invalida")






