from Biblioteca.libroooos import Libros


class Biblioteca:

    def __init__(self, nombre):
        self._nombre = nombre
        self._libros = []


    def agregar_libro(self, titulo,autor,genero):
        libro = Libros(titulo,autor,genero)
        self._libros.append(libro)

    def mostrar_libro(self, libro):
        print(f"libro --> Titulo: {libro.titulo}, Autor: {libro.autor}, Genero: {libro.genero}")

    def buscar_libro_autor(self,autor):
        for libro in self._libros:
            if libro.autor.lower() == autor.lower():
                self.mostrar_libro(libro)

    def buscar_libro_genero(self,genero):
        for libro in self._libros:
            if libro.genero.lower() == genero.lower():
                self.mostrar_libro(libro)

    def mostrar_todos_libros(self):
        print(f"\n***Biblioteca {self._nombre}***")
        for libro in self._libros:
            print(f"""libro id: {libro.id}
            Titulo: {libro.titulo}
            Autor: {libro.autor}
            Genero: {libro.genero}                      
                    """)


