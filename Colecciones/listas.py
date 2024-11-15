print("Manejo de listas")
#
mi_lista = [1,2,3,4,5]
print(f"Lista original {mi_lista}")

#Largo de una lista
print(f"se ocupa el .len {len(mi_lista)}")

#acceder a un elemento en particular
print(f"Con corchetes y el indice, ejemplo: {mi_lista[4]}")

#Modificar elementos
mi_lista[1] = 10
print(f"Modificar valor de la lista {mi_lista[1]}")

#agregar un nuevo valor al final de la lista
mi_lista.append(6)
print(f"Con append se agrega al final de la lista {mi_lista}")

#Agregar un indice en donde quiera
mi_lista.insert(2,15)
print(f"Con insert, primero va el indice y luego el valor que quiero agregar {mi_lista}")

#Eliminar un valor
mi_lista.remove(5)
print(f"Con remove se eliminan elementos, en el indice que quieras {mi_lista}")

#Eliminar un indice
mi_lista.pop(1)
print(f"remueve el elemento del indice {mi_lista}")

#Eliminar con del
del  mi_lista[2]
print(f"Elimina el indice con su elemento {mi_lista}")

#sub listas
sub_lista = mi_lista[1:3]
print(f"Como en las cadenas normales {sub_lista}")


