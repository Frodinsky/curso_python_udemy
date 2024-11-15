from typing import no_type_check
#
print("Este programa hace una reserva en un hotel")

CUARTO_MAR = 190.50
CUARTO_SIN_MAR = 150.50


nombre_usuario = input("Cual es su nombre? ")
dias_estancia = int(input("Cuantos dias estara? "))
cuarto_vista_mar = input("Quiere que su cuarto tenga vista al mar? (Si/NO) ")

cuarto_vista_mar = cuarto_vista_mar.lower().strip() == 'si'

if not cuarto_vista_mar:
    precio_sin_mar = CUARTO_SIN_MAR * dias_estancia
    print(f"""
    \n\t---------------------Detalles de la reservacion-----------------------------\n
    cliente: \t{nombre_usuario}
    dias de estadia: \t{dias_estancia}
    costo total =\t{precio_sin_mar}
    habitacion con vista al mar: No 
    """)
else:
    precio_mar = CUARTO_MAR * dias_estancia
    print(f"""
    \n---------------------Detalles de la reservacion-----------------------------\n
    cliente: \t{nombre_usuario}
    dias de estadia: \t{dias_estancia}
    costo total = \t${precio_mar}
    habitacion con vista al mar: Si
    """)

