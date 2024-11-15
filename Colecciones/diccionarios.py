print("Diccionarios en python")
#
persona = {"nombre":"Sergio",
           "Edad": 30,
           "Ciudad":"México"
           }
#Acceder a los valores

print(f"Nombre: {persona["nombre"]}")
print(f"Edad: {persona.get("Edad")}")
print(f"Ciudad: {persona["Ciudad"]}")

#Modificar un valor del diccionario
persona["Edad"] = 35

#Agregar un nuevo elemento
persona ["profesion: "] = "Ingeniero"

#Eliminar
del persona ["Ciudad"]
persona.pop("profesion")

#aplicar unpacking como en las tuplas

for llave, valor in  persona.items():
    print(f"Llave: {llave} valor: {valor}")

#Optener los valores por separados .key y .value

for llave in persona.keys():
    print(f"Puras llaves: {llave}")