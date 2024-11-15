print("Imprimir el factorial de un numero de manera recursiva")
#
def factorial(numero):
    if numero == 0 or numero == 1:
        print(f"resultado parcial {numero} es: 1")
        return 1
    else:
        factorial_parcial = numero * factorial(numero -1 )
        print(f"Resultado parcial: {numero} es {factorial_parcial}")
        return factorial_parcial


numero_usuario = int(input("Digite el numero para sacar el factor: "))
resultado = factorial(numero_usuario)
