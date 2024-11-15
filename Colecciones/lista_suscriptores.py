print("Lista Suscriptores")
#
#Definimos un set inicial
suscriptores = set()
num_subs = int(input("Cuantos subs tienes?: "))
for _ in range (num_subs):
    suscriptores.add("nuevo suscriptor (email): ")


#Verificar si un suscriptor ya existe
nuevo_sub = input("Proporciona el nuevo sub: ")
if nuevo_sub in suscriptores:
    print(f"El sub ya estaba")
else:
    suscriptores.add(nuevo_sub)
    print(f"Se a agregado el nuevo sub")

#Eliminamos a suscriptores
suscriptores_eliminar = input("Cual suscriptor desea eliminar?")
suscriptores.remove(suscriptores_eliminar)

print("\n",suscriptores)
