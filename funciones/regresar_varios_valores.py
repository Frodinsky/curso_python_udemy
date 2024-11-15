print("***Regresar una tupla de valores desde una funcion***")

#
#definir funcion
def personas_mayusculas(nombre,apellido,edad):
    print(f"Esta funcion regresa una tupla")
    return (nombre.upper(),apellido.upper(),edad)


#programa principal

nombre, apellido, edad = personas_mayusculas("Sandra","jimenez",33)
print(f"Resultado:nombre:{nombre}, apellido: {apellido}, edad: {edad}")

