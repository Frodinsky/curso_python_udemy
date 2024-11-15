print("***Este programa dice si se puede prestar o no un libro***")
#
crendencial = input("Tienes crendencial (Si o No) ")
distancia = int(input("A cuantos KM vives?: "))

prestamo = (crendencial.strip().lower() == 'si'
            or distancia<= 3)

print(f"Se le puede prestar libro: {prestamo} ")









