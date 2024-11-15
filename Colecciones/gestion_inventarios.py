from combinacion_listas_tuplas import producto

print("Este programa gestiona un inventario")

inventario = []


cantidad_productos = int(input("Cuantos articulos deseas agregar? "))

for indice in range(cantidad_productos):
    print(f"Proporciona los valores del producto {indice+1} ")
    Nombre = input("Nombre del producto:")
    Precio = float(input("Costo: "))
    Cantidad = int(input("Cantidad disponible? "))
    #Creaccion del diccionario
    prodcuto = {"id":indice,"nombre":Nombre,"precio":Precio,"Cantidad":Cantidad}
    #agregar el producto al inventario
    inventario.append(prodcuto)
#Mostrar inventario inicial
print(inventario)
#Buscar ID
identificador = int(input("Ingresa el ID del producto que buscas: "))
prodcuto_encontrando = None
for prodcuto in inventario:
    if producto.get("id") == identificador:
        prodcuto_encontrando = prodcuto
        break
if prodcuto_encontrando is not None:
    print("Informacion del producto encontrado")
    




