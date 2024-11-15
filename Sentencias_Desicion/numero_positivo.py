print("***Este programa determina si un numero es positivo***")
#
numero = int(input("Digite un numero: "))

if numero > 0:
    print(f"Este numero es positivo")
elif numero == 0:
    print("Su numero es 0 y por lo tanto no tiene signo")
else:
    print("Su numero es negativo.")
