from Domain.librarie import get_id, to_string
from Logic.CRUD import adauga_vanzare, get_by_id


def print_help():
    print("Comenzi disponibile: ")
    print("Ajutor")
    print("Adauga vanzare: adauga, id, titlu, gen, pret, reducere")
    print("Sterge vanzare: sterge, id")
    print("Afisare: showall")
    print("Stop")
    print("Parametrii trebuie separati prin virgula.")
    print("Comenzile trebuie separate prin ;")


def adauga(lista, parametrii):
    id = str(parametrii[1])
    titlu = str(parametrii[2])
    gen = str(parametrii[3])
    pret = float(parametrii[4])
    reducere = str(parametrii[5])
    lista = adauga_vanzare(id, titlu, gen, pret, reducere, lista)
    return lista


def sterge(lista, parametrii):
    id = int(parametrii[1])
    if get_by_id(id, lista) is None:
        raise ValueError("Nu exista vanzarea cu Id-ul dat")
    return [vanzare for vanzare in lista if get_id(vanzare) != id]


def showall(lista):
    for vanzare in lista:
        print(to_string(vanzare))


def run_console(lista):
    contor = True
    while contor:
        comenzi = input("Introduceti comenzile: ")
        functii = comenzi.split(";")
        for functie in functii:
            parametrii = functie.split(",")
            if parametrii[0] == "Ajutor":
                print_help()
            elif parametrii[0] == "Adauga":
                lista = adauga(lista, parametrii)
            elif parametrii[0] == "Sterge":
                lista = sterge(lista, parametrii)
            elif parametrii[0] == "Afisare":
                print("Lista de vanzari este: ")
                showall(lista)
            elif parametrii[0] == "Stop":
                contor = False
