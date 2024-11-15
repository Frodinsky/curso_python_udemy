#Definimos la clase coche
#
class Coche:
    def __init__(self,marca,modelo,color):
        self._marca = marca #Atributo pretgido
        self._modelo = modelo #Atributo pretegido
        self._color = color #Atributo pretegido


    def conducir(self):
        print(f"""
            Marca: {self._marca}
            Modelo: {self._modelo}
            Color: {self._color}
                """)

    #def get_marca(self):
    #    return self._marca
    #Definir el metodo get de manera pytonica
    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self,marca):
        self._marca = marca
    @property
    def modelo(self):
        return self._modelo
    @modelo.setter
    def modelo(self,modelo):
        self._modelo = modelo
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self,color):
        self._color = color

if __name__ == "__main__":
    coche1 = Coche("Toyota","Yaris","Azul")
    coche1.conducir()
    #Aplicando get y set
    coche1.marca("Toyota2")
    coche1.modelo("Yaris2")
    coche1.color("Blanco")
    coche1.conducir()
