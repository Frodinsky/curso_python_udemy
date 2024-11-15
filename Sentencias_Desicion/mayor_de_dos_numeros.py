from random import randint

numero1 = randint (-100,100)
numero2 = randint (-100,100)
print(numero1, numero2)

if numero1 > numero2:
    print(f"El numero mayor es: {numero1}")
elif numero1 < numero2:
    print(f"El numero mayor es: {numero2}")
else:
    print(f"Ambos numeros son iguales: {numero2, numero1}")