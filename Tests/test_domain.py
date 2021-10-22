from Domain.librarie import creeaza_vanzarea, get_id, get_titlu, get_gen, get_pret, get_reducere


def test_vanzare():
    vanzare = creeaza_vanzarea("1", "Viata lui Pi", "Aventura", 20, "None")
    assert get_id(vanzare) == "1"
    assert get_titlu(vanzare) == "Viata lui Pi"
    assert get_gen(vanzare) == "Aventura"
    assert get_pret(vanzare) == 20
    assert get_reducere(vanzare) == "None"
