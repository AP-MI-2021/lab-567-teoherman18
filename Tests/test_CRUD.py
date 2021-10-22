from Domain.librarie import get_id, get_titlu, get_gen, get_pret, get_reducere
from Logic.CRUD import adauga_vanzare, get_by_id, sterge_vanzare


def test_adauga_vanzare():
    lista = []
    lista = adauga_vanzare("1", "Viata lui Pi", "Aventura", 20, "None", lista)
    assert get_id(get_by_id("1", lista)) == "1"
    assert get_titlu(get_by_id("1", lista)) == "Viata lui Pi"
    assert get_gen(get_by_id("1", lista)) == "Aventura"
    assert get_pret(get_by_id("1", lista)) == 20
    assert get_reducere(get_by_id("1", lista)) == "None"


def test_sterge_vanzare():
    lista = []
    lista = adauga_vanzare("1", "Viata lui Pi", "Aventura", 20, "None", lista)
    lista = adauga_vanzare("2", "Atingerea", "Fantasy", 30, "Silver", lista)

    lista = sterge_vanzare("1", lista)

    assert len(lista) == 1
    assert get_by_id("1", lista) is None
    assert get_by_id("2", lista) is not None


def test_modofica_vanzare():
    pass
