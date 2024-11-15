print("Este programa simula una maquina de snacks")

#Inventario almacen
snack = [
    {"id":1, "nombre":"Chocolate", "Precio":32.00, },
    {"id":2, "nombre":"Coca", "Precio":35.00, },
    {"id":3, "nombre":"chiles", "Precio":65.00, }
]
inventario_ticket = []


def mostrar_snack():
    print("---Invenatio del Almacen---")
    for producto in snack:
        print(f"Id: {producto.get("id")}, Articulo:{producto.get("nombre")}, Precio: {producto.get("Precio")}")

def comprar_snack():
    print("-----Snack comprado----")
    id_buscar = int(input("Que snack quieres? "))
    for producto in snack:
        if producto.get("id") == id_buscar:
            print("\nHas comprado: ")
            print(f"Id: {producto.get("id")} --> Articulo:{producto.get("nombre")} --> Precio: {producto.get("Precio")}")
            inventario_ticket.append(producto)
            return producto
    print("Producto no encontrado")

def mostrar_ticket():
    # Mostrar los artículos en el ticket
    for compra_ticket in inventario_ticket:
        print(f"- Artículo: {compra_ticket.get('nombre')} \t- Precio: {compra_ticket.get('Precio')} ")

    # Calcular la suma total de los precios
    suma_total = sum(compra_ticket["Precio"] for compra_ticket in inventario_ticket)
    print(f"El total de su compra es: {suma_total}")
    return

#Progama principal
if __name__ == "__main__":
    while True:
        print(f"""\n\n\t---tienda snacks ---
        1.-Mostrar snacks
        2.-comprar snacks
        3.-mostrar ticket
        4.-Salir
        """)
        opcion = int(input("Que opcion quiere? (1-4)\n"))
        #revisar opciones del menu
        if opcion == 1:
            mostrar_snack()
        elif opcion == 2:
            comprar_snack()
        elif opcion == 3:
            mostrar_ticket()
        elif opcion == 4:
            print("Hasta pronto")
            break

        else:
            print("Opcion invalida")

