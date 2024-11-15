print("*** Break y continue ***")

#Ejemplo Break
for numero in range (1,10):
    if numero % 2 == 0:
        print(numero)
        break #Rompe al encontrar el primer numero par

#Ejemplo continue
for numero in range(1,10):
    if numero % 2 == 1:
        print(numero)
        continue #Lo que hace aqui es continuar imprimiendo los numeros pares



