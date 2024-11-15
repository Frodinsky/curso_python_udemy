print("***Este programa da el area y perimetro de un rectangulo***")

base = float(input("Digite la base del rectangulo: "))
altura = float(input("Digita la altura del rectangulo: "))

area = base * altura
perimetro = 2 * (area+base)

print(f"""
Aqui estan los resultados del rectangulo
perimetro: {perimetro:.2f}
area: {area:.2f}

""")






