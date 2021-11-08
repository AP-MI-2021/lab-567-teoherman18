from Domain.librarie import to_string
from Logic.CRUD import adauga_vanzare, sterge_vanzare, modifica_vanzare
from Logic.Functionalitati import aplicare_discount, ordine_crescatoare, pret_minim, modifica_genul, titluri_distincte


def print_menu():
    print("1. Adaugare vanzare")
    print("2. Stergere vanzare")
    print("3. Modificare vanzare")
    print("4. Aplica discount in functie de reducerea clientului")
    print("5. Modifica genul pentru un titlu dat")
    print("6. Determina pretul minim pentru fiecare gen")
    print("7. Ordoneaza crescator dupa pret")
    print("8. Afișeaza numărul de titluri distincte pentru fiecare gen.")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare vanzari")
    print("x. Iesire")


def ui_adauga_vanzare(lista, undo_list, redo_list):
    try:
        id = input("Dati id-ul: ")
        titlu = input("Dati titul cartii: ")
        gen = input("Dati genul cartii: ")
        pret = float(input("Dati pretul cartii: "))
        reducere = input("Ce fel de reducere a avut clientul? ")
        rezultat = adauga_vanzare(id, titlu, gen, pret, reducere, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_sterge_vanzare(lista, undo_list, redo_list):
    try:
        id = input("Dati id-ul vanzarii de sters: ")
        rezultat = sterge_vanzare(id, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_modifica_vanzare(lista, undo_list, redo_list):
    try:
        id = input("Dati id-ul vanzarii de modificat: ")
        titlu = input("Dati noul titu: ")
        gen = input("Dati noul gen: ")
        pret = float(input("Dati noul pret: "))
        reducere = input("Dati noul tip de reducere: ")
        rezultat = modifica_vanzare(id, titlu, gen, pret, reducere, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def show_all(lista):
    for vanzare in lista:
        print(to_string(vanzare))


def ui_aplicare_discount(lista, undo_list, redo_list):
    rezultat = aplicare_discount(lista)
    undo_list.append(lista)
    redo_list.clear()
    return rezultat


def ui_ordine_crescatoare(lista, undo_list, redo_list):
    rezultat = ordine_crescatoare(lista)
    undo_list.append(lista)
    redo_list.clear()
    return rezultat


def ui_pret_minim(lista):
    rezultat = pret_minim(lista)
    for gen in rezultat:
        print("Pretul minim pentru genul {} este {}".format(gen, rezultat[gen]))


def ui_modifica_genul(lista, undo_list, redo_list):
    titlu = input("Introduceti titlul cartii al carei gen doriti sa il modificati: ")
    gen_nou = input("Introduceti noul gen: ")
    rezultat = modifica_genul(titlu, gen_nou, lista)
    undo_list.append(lista)
    redo_list.clear()
    return rezultat


def ui_titluri_distincte(lista):
    perechi = titluri_distincte(lista)
    for gen, nr_titluri in perechi:
        print(f"{gen}: {nr_titluri}")


def run_menu(lista):
    undo_list = []
    redo_list = []
    while True:
        print_menu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = ui_adauga_vanzare(lista, undo_list, redo_list)
        elif optiune == "2":
            lista = ui_sterge_vanzare(lista, undo_list, redo_list)
        elif optiune == "3":
            lista = ui_modifica_vanzare(lista, undo_list, redo_list)
        elif optiune == "4":
            lista = ui_aplicare_discount(lista, undo_list, redo_list)
        elif optiune == "5":
            lista = ui_modifica_genul(lista, undo_list, redo_list)
        elif optiune == "6":
            ui_pret_minim(lista)
        elif optiune == "7":
            lista = ui_ordine_crescatoare(lista, undo_list, redo_list)
        elif optiune == "8":
            ui_titluri_distincte(lista)
        elif optiune == "u":
            if len(undo_list) > 0:
                redo_list.append(lista)
                lista = undo_list.pop()
            else:
                print("Nu se poate face undo!")
        elif optiune == "r":
            if len(redo_list) > 0:
                undo_list.append(lista)
                lista = redo_list.pop()
            else:
                print("Nu se poate face redo!")
        elif optiune == "a":
            show_all(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")
