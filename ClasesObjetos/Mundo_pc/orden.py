class Orden:

    contador_orden = 0

    def __init__(self, computadoras):
        Orden.contador_orden += 1
        self.id_orden = Orden.contador_orden
        #Recibimos la lista de tipo computadoras
        self.computadoras = computadoras

    def agregar_computadora(self, computadora):
        self.computadoras.append(computadora)

    def __str__(self):

        computadora_str = ''

        for computadora in self.computadoras:
            computadora_str += "\n" + computadora.__str__()

        return f"""Orden {self.id_orden}
                    Computadoras: {computadora_str}"""

