print("Este programa te dice si una numero es par o impar")
#
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
#llamamos a la funcion

if __name__ == "__main__":
    numero = int(input("Digite el numero: "))
    print(f"Numero par? {es_par(numero)}")
