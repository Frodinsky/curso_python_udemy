print("***Este programa valida una contraseña de 6 caracteres***")

#cadena = 'Hola, Mundo!'
#largo_cadena = len(cadena)
#print (largo_cadena)

contraseña = len(input("Digite su contraseña: "))


while contraseña < 6:
    print("Digitos insuficientes")
    contraseña = len(input("Digite una nueva contraseña"))
else:
    print(f"Contraseña segura")





