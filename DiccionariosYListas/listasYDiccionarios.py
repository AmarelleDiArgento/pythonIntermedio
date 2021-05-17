def run():
    lista  = [1,"Hola",True,4.5]
    diccionario = {"nombres": "un nombre", "apellidos": "un apellido"}

    super_diccionario = {
        "lista 1": lista,
        "lista 2": lista,
    }
    super_lista = [
        {diccionario},
        {diccionario}
    ]
    
    for key, value in super_diccionario.items():
        print(key, " - ", value)


if __name__ == '__main__':
    run()
