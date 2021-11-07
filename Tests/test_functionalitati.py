from Domain.librarie import get_pret
from Logic.CRUD import adauga_vanzare, get_by_id
from Logic.Functionalitati import aplicare_discount, ordine_crescatoare, pret_minim, titluri_distincte


def test_aplicare_discount():
    lista = []
    lista = adauga_vanzare("1", "Ion", "Actiune", 25.50, "None", lista)
    lista = adauga_vanzare("2", "Harry Potter", "Fictiune", 30, "Silver", lista)
    lista = adauga_vanzare("3", "O scrisoare pieduta", "Comedie", 15, "Gold", lista)
    lista = aplicare_discount(lista)
    assert get_pret(get_by_id("1", lista)) == 25.50
    assert get_pret(get_by_id("2", lista)) == 28.50
    assert get_pret(get_by_id("3", lista)) == 13.50


def test_ordine_crescatoare():
    lista = []
    lista = adauga_vanzare("1", "Ion", "Actiune", 25.50, "None", lista)
    lista = adauga_vanzare("2", "Harry Potter", "Fictiune", 30, "Silver", lista)
    lista = adauga_vanzare("3", "O scrisoare pieduta", "Comedie", 15, "Gold", lista)
    lista = [vanzare["pret"] for vanzare in ordine_crescatoare(lista)]
    assert lista == [15, 25.50, 30]


def test_pret_minim():
    lista = []
    lista = adauga_vanzare("1", "Ion", "Fictiune", 25.50, "None", lista)
    lista = adauga_vanzare("2", "Harry Potter", "Fictiune", 30, "Silver", lista)
    lista = adauga_vanzare("3", "O scrisoare pieduta", "Comedie", 15, "Gold", lista)
    rezultat = pret_minim(lista)
    assert len(rezultat) == 2
    assert rezultat["Fictiune"] == 25.50
    assert rezultat["Comedie"] == 15


def test_titluri_distincte():
    lista = []
    lista = adauga_vanzare("1", "Ion", "Realist", 20.0, "None", lista)
    lista = adauga_vanzare("2", "Ion", "Realist", 20.0, "Silver", lista)
    lista = adauga_vanzare("3", "Moara cu noroc", "Fictiune", 25.50, "None", lista)
    lista = adauga_vanzare("4", "Harry Potter", "Fictiune", 30, "Silver", lista)
    lista = adauga_vanzare("5", "O scrisoare pieduta", "Comedie", 15, "Gold", lista)
    lista = adauga_vanzare("6", "Moara cu noroc", "Fictiune", 25.50, "None", lista)
    lista = adauga_vanzare("7", "Harry Potter", "Fictiune", 30, "Silver", lista)
    lista = adauga_vanzare("8", "O scrisoare pieduta", "Comedie", 15, "Gold", lista)
    assert titluri_distincte(lista) == [("Realist", 1), ("Fictiune", 2), ("Comedie", 1)]
