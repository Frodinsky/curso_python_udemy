print("Programa con listas y diccionarios")
#
personas = [
    {
        "nommbre":"Regina",
        "apellido":"Flores",
        "edad": 21
    },
    {
        "nommbre":"Alejandro",
        "apellido":"Reyes",
        "edad": 32
    }
]
print(personas)

#Acceder a un diccionario desde una lista
print(f"""
    Nombre: {personas[0].get("nommbre")}
    Apeliido: {personas[0].get("apellido")}
    Edad: {personas[0].get("edad")}
""")

#recorrer los elementos de la lista
for contador, persona in enumerate(personas):
    print(f"{contador+1} - Persona {persona}")




