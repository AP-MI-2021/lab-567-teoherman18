def creeaza_vanzarea(id, titlu, gen, pret, reducere):
    """
    Creeaza un dictionar ce reprezinta o vanzare.
    :param id: string
    :param titlu: string
    :param gen: string
    :param pret: float
    :param reducere: string
    :return: Un dictionar ce contine o vanzare.
    """
    return {
        "id": id,
        "titlu": titlu,
        "gen": gen,
        "pret": pret,
        "reducere": reducere
    }


def get_id(vanzare):
    """
    Da id-ul unei vanzari.
    :param vanzare: dictionar ce contine o vanzare
    :return: id-ul vanzarii
    """
    return vanzare["id"]


def get_titlu(vanzare):
    """
    Da titlul unei carti.
    :param vanzare: dictionar ce contine o vanzare
    :return: titlul cartii
    """
    return vanzare["titlu"]


def get_gen(vanzare):
    """
    Da genul unei carti.
    :param vanzare: dictionar ce contine o vanzare
    :return: genul cartii
    """
    return vanzare["gen"]


def get_pret(vanzare):
    """
    Da pretul unei carti.
    :param vanzare: dictionar ce contine o vanzare
    :return: pretul cartii
    """
    return vanzare["pret"]


def get_reducere(vanzare):
    """
    Da tipul reducerii pe care a avut-o clientul.
    :param vanzare: dictionar ce contine o vanzare
    :return: tipul reducerii
    """
    return vanzare["reducere"]


def to_string(vanzare):
    return "Id: {}, Titlu: {}, Gen: {}, Pret: {}, Reducere: {}".format(
        get_id(vanzare),
        get_titlu(vanzare),
        get_gen(vanzare),
        get_pret(vanzare),
        get_reducere(vanzare)
    )
