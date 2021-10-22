def print_menu():
    print("1. Adaugare vanzare")
    print("2. Stergere vanzare")
    print("3. Modificare vanzare")
    print("a. Afisare vanzari")
    print("x. Iesire")


def run_menu(lista):
    while True:
        print_menu()
        optiune = input("Dati optiunea: ")