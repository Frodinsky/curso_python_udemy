print("***Generador de correo electronico***")

nombre = input("Digite su  nombre: ")
apellido = input("Digite su  apellido: ")
empresa = input("Digite el nombre de la empresa: ")
dominio = ".com.mz"

nombre_punto = nombre.lower().replace(" ", ".")
apellido_punto = apellido.lower().replace(" ", ".")
empresa_sin_espacios = empresa.lower().replace(" ", "")

correo = nombre_punto + "."+ apellido_punto + "@" + empresa_sin_espacios + dominio

print(f"Su nuevo correo es: {correo}")

