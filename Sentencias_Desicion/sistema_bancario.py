pregunta = input("Desea salir del sistema? (Si/No) ")
#
pregunta_boolean = pregunta.strip().lower() == 'si'

if not pregunta_boolean:
    print("Saliendo del sistema")
else:
    print("Quedando dentro del sistema")