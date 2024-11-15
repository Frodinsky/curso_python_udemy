print("***Sistema de descuento VIP***")

NO_productos_descuentos = 10
cantidad_productos = int(input("Cuantos productos lleva? "))
tiene_membresia = input("Tienes la membresia vip (Si/No)")

es_elegible_descuento = (cantidad_productos >= NO_productos_descuentos
                         and tiene_membresia.strip().lower() == 'si'
                         )

print(f"Tiene acceso al descuento? {es_elegible_descuento}")




