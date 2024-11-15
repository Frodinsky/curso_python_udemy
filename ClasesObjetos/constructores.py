class Persona:

    #Constructor
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f""" Persona: 
                Nombre: {self.nombre}
                apellido: {self.apellido}                
            """)
        print(f"Direccion de memoria desde self: {id(self)}")
        print(f"Direccion de memoria hex desde self: {hex(id(self))}")

# Creaccion de objetos

if __name__ == "__main__":
    # Creacion de un primer objeto
    persona1 = Persona("Purificacion","Lara")
    persona1.mostrar_persona()
    print(f"Direccion de memoria: {id(persona1)}")
    print(f"Direccion de memoria hex: {hex(id(persona1))}")

    # creacion de segundo objeto
    persona2 = Persona("Cacas","Jinx")
    persona2.mostrar_persona()


