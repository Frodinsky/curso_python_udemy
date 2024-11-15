print("Este es un juego de adivinar un numero")

from random import randint

aleatorio = randint(1,50)
#print(aleatorio)
intentos = 0
jugador_numero = 0

while jugador_numero != aleatorio:
    jugador_numero = int(input("Digite el numero: "))

    if aleatorio > jugador_numero:
        print(f"Tu numero es mayor que el numero secreto: {jugador_numero}")
    elif aleatorio < jugador_numero:
        print(f"Tu numero es menor que el numero secreto: {jugador_numero}")
    #else:
     #   print(f"Tu numero no esta entre el 1 y el 50 {jugador_numero}")

    intentos += 1
else:
    print(f"Adivinaste el numero {aleatorio}, te tomo #{intentos} de intentos")

