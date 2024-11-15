class Persona:

    def inicializar_persona(self,nombre,apellido):
        #creamos atributos clase
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f""" Persona: 
                Nombre: {self.nombre}
                apellido: {self.apellido}                
            """)

#Creaccion de objetos

if __name__ == "__main__":

    #Creacion de un primer objeto
    persona1 = Persona()
    persona1.inicializar_persona("Lala","cacas")
    persona1.mostrar_persona()

    #creacion de segundo objeto
    persona2 = Persona()
    persona2.inicializar_persona("Ian","Rodriguez")
    persona2.mostrar_persona()



