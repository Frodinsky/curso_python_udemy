USUARIO = 'Cacas'
CONTRASENA = 'CACAS21'
#
datos_usuario = input("Digite su usuario: ")
datos_contrasena = input("Digite su contraseña: ")

if USUARIO == datos_usuario and CONTRASENA == datos_contrasena:
    print("Bienvenido al sistema")
elif USUARIO != datos_usuario and CONTRASENA == datos_contrasena:
    print(f"Usuario invalido {datos_usuario}")
elif USUARIO == datos_usuario and CONTRASENA != datos_contrasena:
    print(f"Contraseña invalida")
else:
    print("Todo esta mal")