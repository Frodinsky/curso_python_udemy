print("Este programa tiene un modulo recursivo para sacar la potencia de un nuemero")

def potencia_recursiva(numero_base,exponente = 1):
    if exponente == 0:
        #print(f"Resultado es 1")
        return 1
    elif numero_base == 0:
        print(f"Resultado es 0")
        return 0
    else:
        potencia_parcial = numero_base * potencia_recursiva(numero_base, exponente -1)
        print(f"{exponente}.- Resultados parciales {potencia_parcial}")
        return potencia_parcial

base = 2
elevado = 11
resultado = potencia_recursiva(base,elevado)
