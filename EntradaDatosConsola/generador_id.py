from random import randint
print("Este programa genera un ID unico")

nombre = input("Digite su primer nombre: ")
apellido = input("Digite su primer apellido: ")
nacimiento = input("Digite el año en que nacio: ")

sub_nombre = nombre [0:2].upper()
sub_apellido = apellido [0:2].upper()
sub_nacimiento = nacimiento [2:4]
numero_aleatorio = randint (1000,9999).__str__()

identificador = sub_nombre+sub_apellido+sub_nacimiento+numero_aleatorio

print(f"Su curp seria: {identificador}")

#