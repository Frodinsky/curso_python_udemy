print("***Casa de los espejos***")

edad = int(input("Que edad tienes? "))
miedo = input("Le tienes miedo a la oscuridad? (si/no)")

miedo_boolean = miedo.strip().lower() == 'si'

if edad > 10 and miedo_boolean != 'si':
    print("Puedes entrar")
else:
    print("No puedes entrar")