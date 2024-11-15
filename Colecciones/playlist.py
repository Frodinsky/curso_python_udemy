lista_reproduccion = []

numero_canciones = int(input("Cuantas canciones vas a agregar? "))

for indice in range(numero_canciones):
    cancion = input(f"Nombre de la cancion: {indice+1}) ")
    lista_reproduccion.append(cancion)


#orderar lista
lista_reproduccion.sort()

#Lista iterada
for iteraccion in lista_reproduccion:
    print("-",iteraccion)

