class AritmeticaEncapsulamiento:
#
    def __init__(self, operador1, operador2):
        self._operador1 = operador1
        self._operador2 = operador2

    #suma
    def suma(self):
        resultado_suma = self._operador1 + self._operador2
        return resultado_suma
    def resta(self):
        resultado_resta = self._operador1 - self._operador2
        return resultado_resta
    def multiplicacion(self):
        resultado_multi = self._operador1 * self._operador2
        return resultado_multi
    def resultado(self):
        print(f"""Calculadora artimetica con clases y encapsulameinto
        -----
        primer valor = {self._operador1}
        segundo valor = {self._operador2}
        -----
        Suma  = {self.suma()}
        Resta = {self.resta()}
        Multiplicacion = {self.multiplicacion()}
                """)

    @property
    def operador1(self):
        return self._operador1
    @operador1.setter
    def operador1(self,operador1):
        self._operador1 = operador1

    @property
    def operador2(self):
        return self._operador2

    @operador1.setter
    def operador1(self, operador2):
        self._operador2 = operador2


if __name__ == "__main__":
    numeros = AritmeticaEncapsulamiento(5,7)
    numeros.resultado()

    numeros2 = AritmeticaEncapsulamiento(12,16)
    numeros2.resultado()

