class Animal:
#
    def comer(self):
        print("Como muchs veces")

    def dormir(self):
        print("Duermo muchas horas al dia")

class Perro(Animal):
    def hacer_sonido(self):
        print("Se ladrar")
    def dormir(self):
        print("Duermo 15 horas al dia") #sobreescribir

print("***Ejemplo herencia***")
print("Clase padre, soy un animal")

animal1 = Animal()
animal1.dormir()
animal1.comer()
print("\nClase hija, sobrescritura")
perro1 = Perro()
perro1.comer()
perro1.hacer_sonido()
perro1.dormir()
