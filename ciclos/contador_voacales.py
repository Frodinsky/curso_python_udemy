# Paso 1: Definir la cadena de texto
cadena = "Ingresa un texto: "

# Paso 2: Inicializar el contador
contador_vocales = 0

# Paso 3: Crear un conjunto de vocales
vocales = "Te amo osita"

# Paso 4: Iterar sobre cada carácter en la cadena
for caracter in cadena:
    # Paso 5: Contar las vocales
    if caracter in vocales:
        contador_vocales += 1

# Paso 6: Imprimir el resultado
print("Número de vocales:", contador_vocales)
