from ClasesObjetos.Mundo_pc.dispositivo_entrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contador_teclado = 0

    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclado += 1
        self.id_teclado = Teclado.contador_teclado
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return (f"Id: {self.id_teclado}, Marca: {self.marca}, "
                f"Tipo de entrada {self.tipo_entrada}")
