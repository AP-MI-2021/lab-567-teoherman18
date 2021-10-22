from Domain.librarie import to_string
from Logic.CRUD import adauga_vanzare, sterge_vanzare, modifica_vanzare
from Logic.Functionalitati import aplicare_discount


def print_menu():
    print("1. Adaugare vanzare")
    print("2. Stergere vanzare")
    print("3. Modificare vanzare")
    print("4. Aplica discount in functie de reducerea clientului")
    print("a. Afisare vanzari")
    print("x. Iesire")


def ui_adauga_vanzare(lista):
    id = input("Dati id-ul: ")
    titlu = input("Dati titul cartii: ")
    gen = input("Dati genul cartii: ")
    pret = float(input("Dati pretul cartii: "))
    reducere = input("Ce fel de reducere a avut clientul? ")
    return adauga_vanzare(id, titlu, gen, pret, reducere, lista)


def ui_sterge_vanzare(lista):
    id = input("Dati id-ul vanzarii de sters: ")
    return sterge_vanzare(id, lista)


def ui_modifica_vanzare(lista):
    id = input("Dati id-ul vanzarii de modificat: ")
    titlu = input("Dati noul titu: ")
    gen = input("Dati noul gen: ")
    pret = float(input("Dati noul pret: "))
    reducere = input("Dati noul tip de reducere: ")
    return modifica_vanzare(id, titlu, gen, pret, reducere, lista)


def show_all(lista):
    for vanzare in lista:
        print(to_string(vanzare))


def ui_aplicare_discount(lista):
    return aplicare_discount(lista)


def run_menu(lista):
    while True:
        print_menu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = ui_adauga_vanzare(lista)
        elif optiune == "2":
            lista = ui_sterge_vanzare(lista)
        elif optiune == "3":
            lista = ui_modifica_vanzare(lista)
        elif optiune == "4":
            lista = ui_aplicare_discount(lista)
        elif optiune == "a":
            show_all(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")
