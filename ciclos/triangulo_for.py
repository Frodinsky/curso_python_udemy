print("Este programa genera un triangulo o un arbol con el ciclo for")

numero_filas = int(input("Cuantas filas vas a querer? "))

#iterar sobre cada fila del triangulo

for fila in range(1, numero_filas+1):
    espacion_blanco = '-_' * (numero_filas - fila)
    asteriscos = '***' * (2 * fila -1)
    print(espacion_blanco,asteriscos)