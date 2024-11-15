print("Este programa es un sistema de inventarios con un menu, con funciones")
3
#Inventario almacen
inventario = [
    {"id":1, "nombre":"Camisa", "Precio":350.00, "Cantidad":10},
    {"id":2, "nombre":"Pantalon", "Precio":250.00, "Cantidad":6},
    {"id":3, "nombre":"tenis", "Precio":750.00, "Cantidad":2}
]



#Funcion de mostrar inventario
def mostrar_inventario():
    print("---Invenatio del Almacen---")
    for producto in inventario:
        print(f"Id: {producto.get("id")}, Articulo:{producto.get("nombre")}, Precio: {producto.get("Precio")}, Stok: {producto.get("Cantidad")}")

def agregar_producto():
    print("\n\n\n-----Agregar Nuevo Producto----")
    id = int(input("Digte el id: "))
    nombre = input("Digite el nombre del producto: ")
    precio = float(input("Digite el precio del producto: $"))
    cantidad = int(input("Digite la cantidad de productos: "))
    nuevo_producto = {"id":id,"nombre":nombre,
                      "Precio":precio,"Cantidad":cantidad}
    inventario.append(nuevo_producto)
    print("Producto agregado al inventario")

def buscar_producto_id():
    print("\n\n\n-----Buscar producto ID----")
    id_buscar = int(input("Ingresa el ID que buscas: "))
    for prodcuto in inventario:
        if prodcuto.get("id") == id_buscar:
            print("\nInformacion del producto entrado: ")
            print(f"Id: {prodcuto.get("id")}, Articulo:{prodcuto.get("nombre")}, Precio: {prodcuto.get("Precio")}, Stok: {prodcuto.get("Cantidad")}")
            return
    print("Producto no encontrado")

#Progama principal
if __name__ == "__main__":
    while True:
        print(f"""\n\n\t---Menu inventario ---
        1.-Mostrar inventario
        2.-Agregar un nuevo elemento
        3.-Buscar un nuevo elemento
        4.-Salir
        """)
        opcion = int(input("Que opcion quiere? (1-4)\n"))
        #revisar opciones del menu
        if opcion == 1:
            mostrar_inventario()
        elif opcion == 2:
            agregar_producto()
        elif opcion == 3:
            buscar_producto_id()
        elif opcion == 4:
            print("Hasta pronto")
            break
        else:
            print("Opcion invalida")

