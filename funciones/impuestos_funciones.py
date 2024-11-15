print("Funcion de una calculadora de impuestos")

def calculadora_impuesto(pago_sin_impuestos, impuesto):
    pago_total = pago_sin_impuestos + pago_sin_impuestos * (impuesto/100)
    return pago_total

pago_sin_impuestos = 1000
impuesto = 14
pago_con_impuestos = calculadora_impuesto(pago_sin_impuestos, impuesto)
print(pago_con_impuestos)