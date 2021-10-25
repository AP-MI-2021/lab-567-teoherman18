from Domain.librarie import get_pret
from Logic.CRUD import adauga_vanzare, get_by_id
from Logic.Functionalitati import aplicare_discount


def test_aplicare_discount():
    lista = []
    lista = adauga_vanzare("1", "Ion", "Actiune", 25.50, "None", lista)
    lista = adauga_vanzare("2", "Harry Potter", "Fictiune", 30, "Silver", lista)
    lista = adauga_vanzare("3", "O scrisoare pieduta", "Comedie", 15, "Gold", lista)
    lista = aplicare_discount(lista)
    assert get_pret(get_by_id("1", lista)) == 25.50
    assert get_pret(get_by_id("2", lista)) == 28.50
    assert get_pret(get_by_id("3", lista)) == 13.50



