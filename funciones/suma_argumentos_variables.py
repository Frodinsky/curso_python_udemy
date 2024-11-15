print("Suma con argumentos variables")
#
#funcion sumar que acepta argumentos variables
def sumar(*args):
    total = 0
    for numero in args:
        total += numero
    return total

#llamamos a la funcion de sumar
resultado = sumar(1,2,3,4,5,6,7,8,9)
print(f"Resultado de la suma {resultado}")


