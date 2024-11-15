print("***Este programa genera un promedio de calificaciones***")

lista_calificaciones = []
cantidad_calificaciones = int(input("Cuantas calificaciones tienes? "))

for i in range(cantidad_calificaciones):
    calificacion = int(input(f"Digite la calificacion #{i+1}: "))
    lista_calificaciones.append(calificacion)

suma_calificaciones =  sum(lista_calificaciones)
promedio = suma_calificaciones / cantidad_calificaciones

print(f"Promedio = {promedio}")



