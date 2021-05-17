def run():
    limite = 100
    exponente = 2
    # lista = []
    # for i in range(1,limite+1):
    #     val = pow(i,exponente)
    #     if  (i % 3) != 0 :
    #         print(i, "^",exponente, ": ",  pow(i,exponente))
    #         lista.append(val)
    lista = [pow(i,exponente) for i in range(1, (limite +1)) if i % 3 != 0]
                
    print(lista)




if __name__ == "__main__":
    run()