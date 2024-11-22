class Monitor:
    contador_monitores = 0

    def __init__(self, marca, pulgadas):
        Monitor.contador_monitores += 1
        self.id_monitor = Monitor.contador_monitores
        self.marca = marca
        self.pulgadas = pulgadas

    def __str__(self):
        return (f"Id: {self.id_monitor}, Marca: {self.marca},"
                f"Pulgadas: {self.pulgadas}")
