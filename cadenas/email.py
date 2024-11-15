#***Emula generar un email***

nombre = 'Jinx Loca Loquilla'
empresa = 'Lumaca C3 Shop'
dominio = '.com.mx'

nombre_usuario = nombre.replace(' ','.')
nombre_empresa = empresa.replace(' ','.')

email = nombre_usuario + '@' + nombre_empresa + dominio
email = email.lower()

print(f"Este es tu nombre correo: {email}")
#