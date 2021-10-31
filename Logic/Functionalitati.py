from Domain.librarie import get_reducere, creeaza_vanzarea, get_id, get_titlu, get_gen, get_pret


# 4.2
def aplicare_discount(lista):
    """
    Aplica un discount de 5% pentru toate reducerile silver și 10% pentru toate reducerile gold.
    :param lista: lista de vanzari
    :return: noua lista de vanzari, modificata
    """
    lista_noua = []
    for vanzare in lista:
        if get_reducere(vanzare) == "Silver":
            vanzare_noua = creeaza_vanzarea(
                get_id(vanzare),
                get_titlu(vanzare),
                get_gen(vanzare),
                get_pret(vanzare) * 19 / 20,
                get_reducere(vanzare)
            )
            lista_noua.append(vanzare_noua)
        elif get_reducere(vanzare) == "Gold":
            vanzare_noua = creeaza_vanzarea(
                get_id(vanzare),
                get_titlu(vanzare),
                get_gen(vanzare),
                get_pret(vanzare) * 9 / 10,
                get_reducere(vanzare)
            )
            lista_noua.append(vanzare_noua)
        else:
            lista_noua.append(vanzare)
    return lista_noua


# 4.4
def pret_minim(lista):
    """
    Determina prețului minim pentru fiecare gen
    :param lista: lista vanzarilor
    :return: pretul minim pentru fiecare gen
    """
    rezultat = {}
    for vanzare in lista:
        gen = get_gen(vanzare)
        pret = get_pret(vanzare)
        if gen in rezultat:
            if pret < rezultat[gen]:
                rezultat[gen] = pret
        else:
            rezultat[gen] = pret
    return rezultat


# 4.5
def ordine_crescatoare(lista):
    """
    Ordoneaza vânzările crescător după preț.
    :param lista: lista vanzarilor
    :return: lista vanzarilor ordonata crescator dupa pret
    """
    lista_noua = sorted(lista, key=lambda vanzare: get_pret(vanzare))
    return lista_noua
