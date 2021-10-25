from Tests.test_CRUD import test_adauga_vanzare, test_sterge_vanzare, test_modifica_vanzare
from Tests.test_domain import test_vanzare
from Tests.test_functionalitati import test_aplicare_discount


def run_all_tests():
    test_vanzare()
    test_adauga_vanzare()
    test_sterge_vanzare()
    test_modifica_vanzare()
    test_aplicare_discount()

