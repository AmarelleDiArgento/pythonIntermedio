def divisores(number):
    assert number > 0,  "!Ey¡, trabajamos solo con numeros positivos"
    divisoresDe = []
    for i in range(1, (number + 1)):
        if number % i == 0:
            divisoresDe.append(i)
    return divisoresDe

def run():
    try: 
        num = int(input("Digita un numero y yo te dire sus divisores: "))
        print(divisores(num)) 
        print("Listo!, terminamos.")
    except ValueError:
        print("¡Ey!, eso no es un numero.")
        # num = input("Digita un numero y yo te dire sus divisores: ")
        # assert num.isnumeric(), "¡Ey!, eso no es un numero."
        # print(divisores(int(num))) 


if __name__ == "__main__":
    run()