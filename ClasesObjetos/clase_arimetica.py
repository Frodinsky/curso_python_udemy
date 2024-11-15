print("***Este programa se crea una clase para una calculadora***")

class Aritmetica:

    #Python solamente maneja un constructor que va a hacer el ultimo.

    #Constructor
    def __init__(self, operador1, operador2):
        self.operador1 = operador1
        self.operador2 = operador2

    #Suma
    def suma(self):
        resultado_suma = self.operador1 + self.operador2
        return resultado_suma

    #Resta
    def resta(self):
        resultado_resta = self.operador1 - self.operador2
        return resultado_resta

    #Resultados
    def resultados(self):
        print(f"""
                Suma = {self.suma()}
                Resta = {self.resta()}
                 """)


#Creacion de objetos

if __name__ == "__main__":
    #Creacion de primer objeto
    aritmetica1 = Aritmetica(5, 7)
    aritmetica1.resultados()

    #Creacion de segundo objeto
    aritmetica2 = Aritmetica(12,16)
    aritmetica2.resultados()

    aritmetica3 = Aritmetica(25,13)
    aritmetica3.resultados()





