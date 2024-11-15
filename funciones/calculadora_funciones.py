print("***Este programa es una calculadora donde se ocupan funciones")
#
#variables globales
var1 = 0
var2 = 0

def suma():
    resultado = var1+var2
    print(f"El resulado de la suma es: {resultado}")

def resta():
    resultado = var1 - var2
    print(f"El resulado de la resta es: {resultado}")

def multiplicacion():
    resultado = var1 * var2
    print(f"El resulado de la multiplicacion es: {resultado}")

def division():
    if var2 == 0:
        print(f"No se puede dividir entre 0")
    else:
        resultado = var1 / var2
        print(f"El resulado de la suma es: {resultado}")

#Progama principal
if __name__ == "__main__":
    while True:
        print(f"""\n\n\t---tienda snacks ---
        1.-suma
        2.-resta
        3.-multiplicacion
        4.-division
        5.-salir
        """)
        opcion = int(input("Que opcion quiere? (1-5)\n"))
        var1 = int(input("Digite el numero: "))
        var2 = int(input("Digite el numero: "))

        #revisar opciones del menu
        if opcion == 1:
            suma()
        elif opcion == 2:
            resta()
        elif opcion == 3:
            multiplicacion()
        elif opcion == 4:
            division()
        elif opcion == 5:
            print("bye")
            break
        else:
            print("Opcion invalida")
