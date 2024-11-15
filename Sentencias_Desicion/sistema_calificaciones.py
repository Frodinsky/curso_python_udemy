from random import randint
#
califacion = randint (0,12)
califacion_evaluada = None
if califacion < 6:
    califacion_evaluada = 'F'
elif 6<= califacion <7 :
    califacion_evaluada = 'D'
elif 7 <= califacion <8:
    califacion_evaluada = 'C'
elif 8 <= califacion <9:
    califacion_evaluada = 'B'
elif 9<= califacion <= 10:
    califacion_evaluada = 'A'
else:
    califacion_evaluada = 'Valor desconocido'

print(f"Sacaste de califiacion: {califacion_evaluada ,califacion }")