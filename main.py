from Tests.test_all import run_all_tests
from UI.command_line_console import run_console
from UI.console import run_menu


def print_choose_ui():
    print("1. Console")
    print("2. Command line (functionalitati limitate)")
    print("x. Iesire")


def main():
    lista = []
    run_all_tests()
    while True:
        print_choose_ui()
        optiune = input("Alegeti optiunea: ")
        if optiune == "1":
            run_menu(lista)
        elif optiune == "2":
            run_console(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune invalida!")


if __name__ == '__main__':
    main()
