class Animal():
    def hacer_sonido(self):
        print("Sonido cualquiera")
#
class Dog(Animal):
    def hacer_sonido(self):
        print("Ladrar")

class Cat(Animal):
    def hacer_sonido(self):
        print("Maullar")

#Funcion fuera de las clases
def hacer_sonido(animal):
    animal.hacer_sonido()

#Empieza el programa
print("***Ejmplo polimorfismo***")
print("Clase padre: ")
animal1 = Animal()
hacer_sonido(animal1)
print("Clase perro: ")
dog1 = Dog()
hacer_sonido(dog1)
print("Clase gato: ")
cat1 = Cat()
hacer_sonido(cat1)