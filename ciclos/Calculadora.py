print("***Esta es una calculadora con menu repetitivo")
#
operator1 = 0
operator2 = 0
terminar_calculadora = False

while not terminar_calculadora:
    print("""Calculadora de 2 digitos
    1.- Sumar
    2.- Restar
    3.- Multiplicar
    4.- Dividir
    5.- Salir
    """)
    elegir = int(input("Que operacion vas a realizar? "))

    if elegir == 1:
        operator1 = float(input("Digite el primer numero"))
        operator2 = float(input("Digite el primer numero"))
        print(f"La suma es: {operator1+operator2}")
    elif elegir == 2:
        operator1 = float(input("Digite el primer numero"))
        operator2 = float(input("Digite el primer numero"))
        print(f"La resta es {operator1-operator2}")
    elif elegir == 3:
        operator1 = float(input("Digite el primer numero"))
        operator2 = float(input("Digite el primer numero"))
        print(f"La multiplicacion es: {operator1*operator2}")
    elif elegir == 4:
        operator1 = float(input("Digite el primer numero"))
        operator2 = float(input("Digite el primer numero"))
        if operator2 == 0:
            print(f"No se puede dividir entre {operator2}")
        else:
            print(f"La division es: {operator1/operator2}")
    elif elegir == 5:
        print("Saliendo de la calculadora :)")
        terminar_calculadora = True
    else:
        print("Digite un numero valido")






