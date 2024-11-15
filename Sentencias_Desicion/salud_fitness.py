META_PASOS_DIARIOS = 10000
CALORIA_PASOS_DIAROS = 0.04

nombre = input("Digite su nombre: ")
pasos_diarios = int(input("Cuantos pasos dio hoy? "))

cuenta_calorias_pasos_dados = pasos_diarios * CALORIA_PASOS_DIAROS

llego_meta_pasos = META_PASOS_DIARIOS <= pasos_diarios
llego_meta_pasos_if = "Si" if llego_meta_pasos else "No"

print(f"""
el dia de hoy quemo {cuenta_calorias_pasos_dados:.2F}
cumplio la meta de pasos {llego_meta_pasos_if}
""")