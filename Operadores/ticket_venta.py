print("***Programa que genera un ticket***")
#
precio_leche = float(input("Precio leche: "))
precio_pan = float(input("Precio pan: "))
precio_lechuga = float(input("Precio lechuga: "))
precio_platanos = float(input("Precio platanos: "))
descuento_porcentaje = int(input("De cuanto es el descuento que tienes? "))

#calculo subtotal sin impuestos
subtotal = precio_leche + precio_pan + precio_lechuga + precio_platanos

#Descuento
descuento_porcentaje = subtotal * (descuento_porcentaje/100)

#subTotal con descuento
subtotal_descuento = subtotal - descuento_porcentaje

#calculo con impuestos 16%
impuesto = subtotal_descuento * 0.16

#costo total
costo_total = subtotal_descuento + impuesto

print(f"""
subtotal: ${subtotal:.2f}
descuento: ${descuento_porcentaje:.2f}
impuesto: ${impuesto:.2f}
total: ${costo_total:.2f}
""")