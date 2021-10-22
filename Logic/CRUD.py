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
    lista_noua = []
    for vanzare in lista:
        if get_id(vanzare) == id:
            vanzare_noua = creeaza_vanzarea(id, titlu, gen, pret, reducere)
            lista_noua.append(vanzare_noua)
        else:
            lista_noua.append(vanzare)
    return lista_noua
