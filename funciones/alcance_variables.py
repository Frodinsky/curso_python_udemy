print("Alcance de variables")

#variable global
contador_original = 0

def incremento_contador():
    #declaramos variable local
    contador_local = 0
    global  contador_original
    contador_original +=1

    contador_local +=1

    print(f"Contador local {contador_local}")
    print(f"Contador global {contador_original}\n")

incremento_contador()
incremento_contador()
