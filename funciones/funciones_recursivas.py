print("Imprimir del 1 al 5 de forma recursiva")

def funcion_recursiva(numero):
    #caso base
    if numero == 1:
        print(numero, end= " ")
    else:
        funcion_recursiva(numero-1)
        print(numero, end= " ")

funcion_recursiva(5)
