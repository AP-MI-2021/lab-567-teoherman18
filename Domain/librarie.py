def creeaza_vanzarea(id, titlu, gen, pret, reducere):
    """
    Creeaza o lista ce reprezinta o vanzare.
    :param id: string
    :param titlu: string
    :param gen: string
    :param pret: float
    :param reducere: string
    :return: O lista ce contine o vanzare.
    """
    # return [str(id), str(titlu), str(gen), pret, str(reducere)]

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
    # return vanzare[0]


def get_titlu(vanzare):
    """
    Da titlul unei carti.
    :param vanzare: dictionar ce contine o vanzare
    :return: titlul cartii
    """

    return vanzare["titlu"]
    # return vanzare[1]


def get_gen(vanzare):
    """
    Da genul unei carti.
    :param vanzare: dictionar ce contine o vanzare
    :return: genul cartii
    """
    return vanzare["gen"]
    # return vanzare[2]


def get_pret(vanzare):
    """
    Da pretul unei carti.
    :param vanzare: dictionar ce contine o vanzare
    :return: pretul cartii
    """
    return vanzare["pret"]
    # return vanzare[3]


def get_reducere(vanzare):
    """
    Da tipul reducerii pe care a avut-o clientul.
    :param vanzare: dictionar ce contine o vanzare
    :return: tipul reducerii
    """
    return vanzare["reducere"]
    # return vanzare[4]


def to_string(vanzare):
    return "Id: {}, Titlu: {}, Gen: {}, Pret: {}, Reducere: {}".format(
        get_id(vanzare),
        get_titlu(vanzare),
        get_gen(vanzare),
        get_pret(vanzare),
        get_reducere(vanzare)
    )
