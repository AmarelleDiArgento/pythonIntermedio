
from functools import reduce

def run():
    # Filtros 
    listaBase = [1,4,5,6,9,13,19,21]
    odd = list(filter(lambda x: x%2 != 0, listaBase))
    print(odd)
    #Map
    listaBase = [z for z in range(1,6)]
    # listaAlCuadrado = [pow(i,2) for i in listaBase]
    listaAlCuadrado = list(map(lambda x: pow(x,2), listaBase))
    print(listaAlCuadrado)

    # Reduce
    listaBase = [2 for z in range(1,6)] 
    # for i   in listaBase:
    #     total = total * i
    total = reduce(lambda a,b: a * b,listaBase)

    print(total)
    


if __name__ == "__main__":
    run()