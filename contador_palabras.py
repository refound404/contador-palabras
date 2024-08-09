import string

def contador_de_palabras():
    texto = input("Introduce un texto: ").lower()

    texto = texto.translate(str.maketrans("", "", string.punctuation))

    palabras = texto.split()

    contador= {}

    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1

    print("Resultados: ")
    for palabra, frecuencia in contador.items():
        print(f"{palabra}: {frecuencia}")

contador_de_palabras()