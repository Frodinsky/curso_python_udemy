class Persona:
    atributo_clase = 0

    def __init__(self, atributo_instancia):
        self.atributo_instancia = atributo_instancia


#programa principal

if __name__ == "__main__":
    print("***Atributo de clase***")
    print(f"Atributo de instancia {Persona.atributo_clase}")

    #Modificamos el atributo de clase

    Persona.atributo_clase = 10
    print(f"Modificacion {Persona.atributo_clase}")

    #Creamos primer objeto
    persona1 = Persona(15)
    print("\t-------")
    print(f"Clase {persona1.atributo_clase}")
    print(f"Instancia {persona1.atributo_instancia}")

    #Creamos segundo objeto
    persona2 = Persona(30)
    print("\t-------")
    print(f"Clase {persona2.atributo_clase}")
    print(f"Instancia {persona2.atributo_instancia}")
