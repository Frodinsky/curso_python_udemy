print("***Sistema Empleados***")

nombre_empleado = input("Nombre del empleado: ")
edad_empleado = int(input("Ingresa edad empleado: "))
salario_empleado = float(input("Ingrese salario del empleado: "))
es_jefe_departamteno = input("Es jefe del deparatemento (Si/No)")

#Vamos a convertir str a boolean
es_jefe_departamteno = es_jefe_departamteno.lower() == "si"

#Imprimir los valores de los empleados

print("\nDatos empleado")
print(f"Nombre: {nombre_empleado} ")
print(f"Edad: {edad_empleado}")
print(f"Salario: {salario_empleado}")
print(f"Es jefe de departamento?: {es_jefe_departamteno}")
#