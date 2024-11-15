print("Argumentos variables")

def superheroe_superpoderes(superheroe, nombre, *args):
    print(f"Superheroe: {superheroe} - {nombre} - {args}")
    #iteramos los poderes
    for superpoder in args:
        print(f"\t Superpoder: {superpoder}")


#Llamar la funcion

superheroe_superpoderes("Spiderman","peter parker","instinto aracnido","telaraña","super fuerza")
superheroe_superpoderes("Iron-man","Tony Stark","playboy","Filantropo","Millonario")


