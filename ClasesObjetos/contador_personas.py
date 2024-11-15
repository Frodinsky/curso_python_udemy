class Persona:
    #Atributo de clase
    contador_personas = 0
#
    def __init__(self,nombre,apellido):
        #Incrementa el valor del atributo de clase
        Persona.contador_personas +=1
        self.id = Persona.contador_personas
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f"Persona: {self.id}, {self.nombre}, {self.apellido}")

    @staticmethod
    def get_contador_personas_estatico():
        print(f"Metodo estatico")
        return Persona.contador_personas

    @classmethod
    def get_contador_pesona_clase(cls):
        print("Metodo de clase")
        return cls.contador_personas

if __name__ == "__main__":
    print("***Ejemplo contador de personas***")
    persona1 = Persona("Jinx","Cacas")
    persona1.mostrar_persona()

    persona2 = Persona("Purificacion","Cacas")
    persona2.mostrar_persona()

    print(f"Personas dentro del programa: {Persona.contador_personas}")
    print(f"Con metodo estatico: {Persona.get_contador_personas_estatico()}")
    print(f"Con metodo de clase: {Persona.get_contador_pesona_clase()}")

