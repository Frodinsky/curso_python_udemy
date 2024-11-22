from ClasesObjetos.Mundo_pc.computadora import Computadora
from ClasesObjetos.Mundo_pc.monitor import Monitor
from ClasesObjetos.Mundo_pc.orden import Orden
from ClasesObjetos.Mundo_pc.raton import Raton
from ClasesObjetos.Mundo_pc.teclado import Teclado

print("Mundo pc")

#Computadora 1

teclado1 = Teclado('HP', 'USB')
raton1 = Raton('HP', 'USB')
monitor1 = Monitor('HP', 27)
computadora1 = Computadora('HP', monitor1, teclado1, raton1)

#computadora 2

teclado2 = Teclado('HP', 'USB')
raton2 = Raton('HP', 'USB')
monitor2 = Monitor('HP', 1000)
computadora2 = Computadora('HP', monitor2, teclado2, raton2)

#Lista de computadoras

listas_computadoras1 = [computadora1, computadora2]
orden1 = Orden(listas_computadoras1)

print(orden1)