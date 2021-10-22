from Tests.test_CRUD import test_adauga_vanzare, test_sterge_vanzare
from Tests.test_domain import test_vanzare


def run_all_tests():
    test_vanzare()
    test_adauga_vanzare()
    test_sterge_vanzare()
