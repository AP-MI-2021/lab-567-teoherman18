from Domain.librarie import creeaza_vanzarea, get_id


# 4.1
def adauga_vanzare(id, titlu, gen, pret, reducere, lista):
    """
    Adauga o vanzare intr-o lista.
    :param id: string
    :param titlu: string
    :param gen: string
    :param pret: float
    :param reducere: string
    :param lista: lista de vanzari
    :return: o lista continand atat elementele vechi, cat si noua vanzare
    """
    if get_by_id(id, lista) is not None:
        raise ValueError("Id-ul exista deja!")
    if int(id) < 1:
        raise ValueError("ID-ul nu poate fi nul sau negativ!")
    if len(titlu) == 0:
        raise ValueError("Introduceti titlul!")
    if len(gen) == 0:
        raise ValueError("Introduceti genul!")
    if pret < 0:
        raise ValueError("Pretul nu poate fi negativ!")
    vanzare = creeaza_vanzarea(id, titlu, gen, pret, reducere)
    return lista + [vanzare]


def get_by_id(id, lista):
    """
    Da vanzarea cu id-ul dat dintr-o lista.
    :param id: string
    :param lista: lista de vanzari
    :return: vanzarea cu id-ul dat din lista sau None, daca ea nu exista
    """
    for vanzare in lista:
        if get_id(vanzare) == id:
            return vanzare
    return None


def sterge_vanzare(id, lista):
    """
    Sterge vanzarea cu id-ul dat dintr-o lista.
    :param id: string
    :param lista: lista de vanzari
    :return: lista de vanzari
    """
    if get_by_id(id, lista) is None:
        raise ValueError("Nu exista o vanzare cu id-ul dat!")
    return [vanzare for vanzare in lista if get_id(vanzare) != id]


def modifica_vanzare(id, titlu, gen, pret, reducere, lista):
    """
    Modifica o vanzare dupa id.
    :param id: string
    :param titlu: string
    :param gen: string
    :param pret: float
    :param reducere: string
    :param lista: lista de vanzari
    :return:
    """
    if get_by_id(id, lista) is None:
        raise ValueError("Nu exista o vanzare cu id-ul dat!")
    if len(titlu) == 0:
        raise ValueError("Introduceti titlul!")
    if len(gen) == 0:
        raise ValueError("Introduceti genul!")
    if pret < 0:
        raise ValueError("Pretul nu poate fi negativ!")
    lista_noua = []
    for vanzare in lista:
        if get_id(vanzare) == id:
            vanzare_noua = creeaza_vanzarea(id, titlu, gen, pret, reducere)
            lista_noua.append(vanzare_noua)
        else:
            lista_noua.append(vanzare)
    return lista_noua
