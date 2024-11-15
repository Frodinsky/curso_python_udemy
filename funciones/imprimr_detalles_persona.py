print("Imprimir detalles de una persona utilizando kwargs")

#Funcion que acepta argumentos variables en forma de llave-valor osea en dict (diccionario)
def imprimir_detalle_persona(**kwargs):
    print("\nValores recibidisos")
    for llave,valor in kwargs.items():
        print(f"{llave} - {valor}")

#llamamos a la funcion
imprimir_detalle_persona(nombre = "Karla", edad = 30, Ciudad = "CDMX")
imprimir_detalle_persona(nombre = "Jesus", edad = 18, Ciudad = "Jalisco", puesto = "Gerente")

