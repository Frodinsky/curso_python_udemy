import random


# Inicializar el tablero
def crear_tablero():
    return [["~" for _ in range(5)] for _ in range(5)]


# Colocar barcos
def colocar_barcos(tablero, cantidad_barcos):
    for _ in range(cantidad_barcos):
        while True:
            fila = random.randint(0, 4)
            columna = random.randint(0, 4)
            if tablero[fila][columna] == "~":  # Asegúrate de que esté vacío
                tablero[fila][columna] = "B"
                break


# Disparar
def disparar(tablero, coordenada):
    fila, columna = coordenada
    if tablero[fila][columna] == "B":
        tablero[fila][columna] = "X"  # Golpe
        return "Hit!"
    elif tablero[fila][columna] == "~":
        tablero[fila][columna] = "O"  # Fallo
        return "Miss!"
    else:
        return "Ya disparaste aquí."


# Verificar estado del juego
def verificar_estado(tablero):
    for fila in tablero:
        if "B" in fila:
            return False
    return True


# Convertir coordenada a índices
def coordenada_a_indices(coordenada):
    letra = coordenada[0].upper()  # Convertir a mayúsculas
    numero = int(coordenada[1]) - 1  # Convertir a índice (0-4)

    # Convertir letra a índice
    fila = ord(letra) - ord('A')

    if 0 <= fila < 5 and 0 <= numero < 5:
        return fila, numero
    else:
        return None  # Coordenada fuera de rango


# Función para mostrar el tablero
def mostrar_tablero(tablero):
    print("  1 2 3 4 5")  # Encabezado de columnas
    for i, fila in enumerate(tablero):
        print(chr(i + 65), ' '.join(fila))  # Convertir índice a letra (A, B, C...)


# Inicializar el juego
tablero = crear_tablero()
colocar_barcos(tablero, 3)

# Lógica del juego
while True:
    mostrar_tablero(tablero)  # Muestra el tablero en 2D
    coord = input("Introduce tu disparo (ej. A1): ")
    indices = coordenada_a_indices(coord)

    if indices is None:
        print("Coordenada inválida. Intenta de nuevo.")
        continue

    fila, columna = indices
    resultado = disparar(tablero, (fila, columna))
    print(resultado)

    if verificar_estado(tablero):
        print("¡Has hundido todos los barcos!")
        break
