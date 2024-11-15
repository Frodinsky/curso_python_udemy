print("Argumentos variables en forma de diccionario (dict)")
#
def superheroe_superpoderes(nombre, *args, **kwargs):
    print(f"Superheroes: {nombre} - {args} - Mas info {kwargs}")

superheroe_superpoderes("Spiderman","super fuerza" , edad = 17, empresa="Marvel")


