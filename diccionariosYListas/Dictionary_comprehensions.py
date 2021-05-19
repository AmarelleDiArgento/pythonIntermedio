import math

def run():
    # diccionario = {}
    # for i in range(1,101):
    #     if i % 3 != 0:
    #         diccionario[i] = i**2;

    #diccionario = {i: i**2 for i in range(1,101) if i % 3 != 0}
    diccionario = {i: math.sqrt(i) for i in range(1,1001) if i % 3 != 0}
    print(diccionario)
    

if __name__ == "__main__":
    run()