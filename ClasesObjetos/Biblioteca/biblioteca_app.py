from Biblioteca.biblioteca_alejandria import Biblioteca

print("***\t\tBiblioteca de alejandriaa***")

biblioteca = Biblioteca("Mi Biblioteca")
biblioteca.agregar_libro("Principito","Frances","Infantil")
biblioteca.agregar_libro("1984", "George Orwell", "Ficción")
biblioteca.agregar_libro("Las enseñanzas de don juan","Carlos Castañeda","Antropologia")
biblioteca.agregar_libro("Los juegos del hambre","Susan Colins","Ficción")
biblioteca.agregar_libro("Sinsajo","Susan Colins","Ficción")
print("Libro del autor:")
biblioteca.buscar_libro_autor("Carlos Castañeda")
print("Libros del genero")
biblioteca.buscar_libro_genero("Infantil")
biblioteca.mostrar_todos_libros()