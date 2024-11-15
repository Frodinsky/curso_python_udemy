print('*** Agenda de Contactos ***')
#
agenda = {
    'Carlos': {
        'telefono': '55667711',
        'email': 'carlos@mail.com',
        'direccion': 'Calle Principal 132'
    },
    'María': {
        'telefono': '99887733',
        'email': 'maria@mail.com',
        'direccion': 'Avenida Central 456'
    },
    'Pedro': {
        'telefono': '55139078',
        'email': 'pedro@mail.com',
        'direccion': 'Plaza Mayor 789'
    }
}

print(agenda)

#acceder a la informacion de un contacto en especifico
print(f"""Informacion del contacto de maria:
    Telefono: {agenda["María"]["telefono"]}
    Email: {agenda.get("María").get("email")}
    Direecion: {agenda.get("María").get("direccion")}

""")



