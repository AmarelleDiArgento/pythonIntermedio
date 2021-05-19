def palindromo(string ):
    try:
        if len(string) ==  0:
            raise ValueError("No se puede ingresar una cadena vacia")
        return  string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False    
def run():
    try:
        palabra = input("digita una palabra, yo te dire si es o no, un palindromo: ")
        print(f'... {palabra}... {palindromo(palabra)}')
        if palindromo(palabra):
            print(f'{palabra}, es un palindromo')
        else:
            print(f'{palabra}, NO es un palindromo')
    except TypeError:
        print("Solo se pueden ingresar textos")

if __name__ == "__main__":
    run()