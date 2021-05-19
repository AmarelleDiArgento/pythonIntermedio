    
from typing import List


DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]
def run():
    print("Trabajadores que usan Python:")
    print("List comprehesions:")
    all_python_dev = [trabajador for trabajador in DATA if trabajador["language"] == "python"]
    for trabajador in all_python_dev:
        print(trabajador)

    print("Filter y Map:")
    all_python_dev2 = list(filter(lambda trabajador: trabajador["language"] == "python", DATA))
    all_python_dev2 = list(map(lambda trabajador: trabajador["name"],all_python_dev2))
    for trabajador in all_python_dev2:
        print(trabajador)

    print("Trabajadores de Platzi:")
    print("List comprehesions:")
    all_platzi_workers = [trabajador for trabajador in DATA if trabajador["organization"] == "Platzi"]
    for trabajador in all_platzi_workers:
        print(trabajador)

    print("Filter y Map:")
    all_platzi_workers2 = list(filter(lambda trabajador: trabajador["organization" ] == "Platzi" ,DATA))
    all_python_dev2 = list(map(lambda trabajador: trabajador["name"],all_platzi_workers2))
    for trabajador in all_platzi_workers2:
        print(trabajador)


    print("Trabajadores de Platzi:")
    print("Filter y Map:")
    all_adults = list(filter(lambda  trabajador: trabajador["age"] >= 18, DATA))
    all_adults = list(map(lambda  trabajador: trabajador["name"] , all_adults))
    for trabajador in all_adults:
        print(trabajador)

    print("List comprehesions:")
    all_adults2 = [trabajador for trabajador in DATA if trabajador["age"] >= 18]
    for trabajador in all_adults2:
        print(trabajador)

    
    print("Trabajadores mayores de edad")
    print("Filter y Map:")
    all_adults = list(filter(lambda  trabajador: trabajador["age"] >= 18, DATA))
    all_adults = list(map(lambda  trabajador: trabajador["name"] , all_adults))
    for trabajador in all_adults:
        print(trabajador)

    print("List comprehesions:")
    all_adults2 = [trabajador for trabajador in DATA if trabajador["age"] >= 18]
    for trabajador in all_adults2:
        print(trabajador)

    
    print("Trabajadores de mas de 70 años:")
    print("Filter y Map:")        
    old = list(map(lambda trabajador: trabajador | { "old": trabajador["age"] >= 70}, DATA))
    print(old)
    for trabajador in old:
        print(trabajador)

    print("List comprehesions:")
    old2 = [{**trabajador, **{'old': trabajador['age'] > 70}}  for trabajador in DATA]
    for trabajador in old2:
        print(trabajador)

if __name__ == "__main__":
    run()

