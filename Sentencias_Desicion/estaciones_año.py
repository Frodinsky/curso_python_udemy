from random import randint

numero_estacion = randint (1,12)
print(numero_estacion)

if  2 < numero_estacion < 6:
    print(f"primavera {numero_estacion}")
elif 6 <= numero_estacion < 9:
    print(f"verano {numero_estacion}")
elif 9 <= numero_estacion < 12:
    print(f"otoño {numero_estacion}")
else:
    print(f"invierno {numero_estacion}")

