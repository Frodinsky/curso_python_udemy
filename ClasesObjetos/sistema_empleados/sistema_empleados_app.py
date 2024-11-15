from empleado import Empleado
from empresa import Empresa
#
print("***Sistema de empleados***")

#Crear una instancia de empresa
empresa1 = Empresa("Global Mentoring")

#Contratar empleados
empresa1.contratar_empleado("Juan","Ventas")
empresa1.contratar_empleado("Maria","Marketing")
empresa1.contratar_empleado("Pablo","RH")
empresa1.contratar_empleado("Pedro","Ventas")

print(f"Total de empleados: {Empleado.obtener_total_empleados()}")

#Obtener numero de empleados en el departamento de ventas
print(f"Categoria Ventas: "
      f" {empresa1.obtener_numero_empleados_departamento("Ventas")}")

#mostrar todos los empleados de la empresa

empresa1.obtener_total_empleados()

#crear empresa 2

empresa2 = Empresa("Lumaca")

empresa2.contratar_empleado("Esmeralda","Lenguaje")
empresa2.contratar_empleado("Kari","Conducta")
empresa2.contratar_empleado("Rosi","Jefa")
empresa2.contratar_empleado("Mau","Jefa")
empresa2.contratar_empleado("Paulina","Lenguaje")
empresa2.contratar_empleado("Zuleman","Conducta")

print(f"""
      Total empleados de lumca: {Empleado.obtener_total_empleados()}
      Total empleados de Lenguaje: {empresa2.obtener_numero_empleados_departamento("Lenguaje")}

""")
empresa2.obtener_total_empleados()
