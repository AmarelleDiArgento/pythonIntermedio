# Modos de Apertura

# r -> Solo lectura
# r+ -> Lectura y escritura
# w -> Solo escritura. Sobre escribe el archivo si existe. Crea el archivo si no existe
# w+ -> Escritura y lectura. Sobre escribe el archivo si existe. Crea el archivo si no existe
# a -> Añadido (agregar contenido). Crea el archivo si éste no existe
# a+ -> Añadido (agregar contenido) y lectura. Crea el archivo si éste no existe.


def leer():
    numeros = []
    with open("./archivos/numeros.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            numeros.append(int(linea))
    return numeros

def escribir():
    nombres = ["Jose","Conchita","Paco","Lucero","Antonela","Martina"]
    with open("./archivos/nombres.txt", "w", encoding="utf-8") as archivo:
        for nombre in nombres:
            archivo.write(nombre)
            archivo.write("\n")

def run():
    escribir()
    print(leer())


if __name__ == "__main__":
    run()
