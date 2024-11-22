from ClasesObjetos.Mundo_pc.dispositivo_entrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contador_ratones = 0

    def __init__(self, marca, entrada):
        Raton.contador_ratones += 1
        self.id_raton = Raton.contador_ratones
        #self.marca = marca
        #self.entrada = entrada
        super().__init__(marca, entrada)

    def __str__(self):
        return (f"Id {self.id_raton}, Marca: {self.marca}, "
                f"Tipo entrada: {self.tipo_entrada}  ")

#codigo principal

if __name__ == '__main__':
    raton1 = Raton("HP", "USB 3.0")
    print(raton1)