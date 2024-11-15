print("***Este programa autentifica a un usuario y su contraseña ***")
#
usuario_constante = "Cacas"
constaseña_constante = "23Cacas"

usuario = input("Digite su usuario: ")
contraseña = input("Digite su contraseña: ")

#validacion de datos
user = usuario == usuario_constante
password = contraseña == constaseña_constante

resultado = user and password

print(f"Escribio bien el usuario? {user}")
print(f"Escribio bien la contraseña? {password}")
print(f"Puede entrar: {resultado}")


