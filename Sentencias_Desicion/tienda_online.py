print("***Tienda en linea***")
#
compro = float(input("Digite el precio de su ticket: "))
tiene_vip = input("Es miembro vip? (Si/No) ")

#validar vip
validacion_vip = tiene_vip.lower() == 'si'

if compro >= 1000 and validacion_vip:
    print(f"Tiene un descuento del 15%")
elif compro > 1000:
    print(f"Tiene un descuento de 10%")
elif  tiene_vip == 'si':
    print(f"Tiene un descuento del 5%")
else:
    print(f"No tiene descuento")



