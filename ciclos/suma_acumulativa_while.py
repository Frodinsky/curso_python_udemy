from random import randint

print("***Suma acumulativa ciclo while")
#

#Sumar los primeros 5 numeros

MAXIMO = 100
numero = 0
acumulador_suma = 0

while numero<=MAXIMO:
    acumulador_suma += numero
    numero += 1
    print(f"La suma acumulada {acumulador_suma} la suma numero: {numero}")

print(f"\nLa suma acumulada final {acumulador_suma} ")

#Todo aleatorio

Maximo = randint (30,999)
Numero = randint (0, 9)
Acumulador_suma = 0

while Numero<=Maximo:
    Acumulador_suma += Numero
    Numero += 1

print(f"La suma aleatoria {Acumulador_suma}")
