print("***Convierte grados de celcius a Fahrenheit  y viceversa***")
#
def conversion_celcius():
    conversion = (temperatura*(9/5))+32
    print(f"La temperatura en celcius es: {conversion}")
def conversion_Fahrenheit():
    conversion = (temperatura-32)*(5/9)
    print(f"La temperatura es: {conversion}")


#Progama principal
if __name__ == "__main__":
    while True:
        print(f"""\n\n\t---Conversor de temperatura ---
        1.-Convertir a Celcius
        2.-Convertir a Fahrenheit
        3.-Salir
        """)
        temperatura = float(input("\n\tDigite la temperatura:"))
        opcion = int(input("Que opcion quiere? (1-4)\n"))
        #revisar opciones del menu
        if opcion == 1:
            conversion_celcius()
        elif opcion == 2:
            conversion_Fahrenheit()
        elif opcion == 3:
            print("Hasta pronto")
            break
        else:
            print("Opcion invalida")