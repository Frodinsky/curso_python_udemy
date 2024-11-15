numeros = [1,2,3,4,5,6,7,8,9,10]
cuadrados = [x**2 for x in numeros]
print(cuadrados)
#
#Lista numeros pares
numeros = range(10+1)
pares = [x for x in numeros if x%2 == 0]
print(pares)

#Lista de nombres
nombres = ["Alan","Adaa","asd","sdxzc","vxc"]
saludando = [f"Hola :) {nombre}" for nombre in nombres]
print(saludando)