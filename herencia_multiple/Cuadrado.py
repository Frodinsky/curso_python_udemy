from herencia_multiple.Color import Color
from herencia_multiple.FiguraGeometrica import FiguraGeometrica


class Cuadrado(FiguraGeometrica, Color):

    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho

    def __str__(self):
        #return f'Area del cuadrado = {self.calcular_area()}\nColor = {self.color}'
        return f'Cuadrado es la {FiguraGeometrica.__str__(self)} {Color.__str__(self)} Area = {self.calcular_area()}'

class Rectangulo(FiguraGeometrica, Color):

    def __init__(self, base, lado, color):
        FiguraGeometrica.__init__(self, base, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'Rectangulo es la {FiguraGeometrica.__str__(self)} {Color.__str__(self)} Area = {self.calcular_area()}'




