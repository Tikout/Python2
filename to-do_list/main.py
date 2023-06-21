import json

zadania = {}
temp_id = 0

def add():
    global temp_id
    tytul = input("Podaj tytuł: ")
    opis = input("Podaj opis: ")
    termin = input("Podaj termin: ")
    id = temp_id + 1
    while id in zadania:
        id = id + 1
    temp_id = id
    zadania[temp_id] = {"Tytul": tytul, "Opis": opis, "Termin": termin}

def check():
    if zadania:
        for id, b in zadania.items():
            print("Id:", id)
            print("Tytuł:", b["Tytul"])
            print("Opis:", b["Opis"])
            print("Termin:", b["Termin"])
            print()
    else:
        print("Brak zadań")

def check_desc():
    try:
        try:
            id = int(input("Podaj id: "))
            b = zadania[id]
            print("Opis zadania:", b["Opis"])
        except ValueError:
            print("Nieprawidłowe id")
    except KeyError:
        print("Nieprawidłowe id")

def delete():
    try:
        try:
            id = int(input("Podaj id: "))
            del zadania[id]
        except ValueError:
            print("Nieprawidłowe id")
    except KeyError:
        print("Nieprawidłowe id")

def edit():
    try:
        id = int(input("Podaj id: "))
        if id in zadania:
            tytul = input("Podaj nowy tytuł: ")
            opis = input("Podaj nowy opis: ")
            termin = input("Podaj nowy termin: ")
            zadania[id] = {"Tytul": tytul, "Opis": opis, "Termin": termin}
        else:
            print("Nieprawidłowe id")
    except ValueError:
        print("Nieprawidłowe id")

try:
    with open("plik.json", "r") as infile:
        tasks = json.load(infile)
        if tasks:
            zadania = {int(id): b for id, b in tasks.items()}
            for id, b in zadania.items():
                print("id: ", id)
                print("tytuł: ", b["Tytul"])
                print("termin: ", b["Termin"])
        else:
            print("Brak zadań")
except FileNotFoundError:
    print("Brak zadań")

while True:
    print("*-*-*-*-*")
    print("1. Dodaj zadanie")
    print("2. Sprawdź zadania")
    print("3. Sprawdź opis zadania")
    print("4. Usuń zadanie")
    print("5. Edytuj zadanie")
    print("6. Zapisz do pliku JSON")
    print("7. Zakończ")
    print("*-*-*-*-*")
    a = int(input("Wybierz polecenie: "))
    if a == 1:
        add()
    elif a == 2:
        check()
    elif a == 3:
        check_desc()
    elif a == 4:
        delete()
    elif a == 5:
        edit()
    elif a == 6:
        with open("plik.json", "w") as outfile:
            json.dump(zadania, outfile)
        print("Utworzono plik JSON!")
    elif a == 7:
        print("Koniec programu.")
        break
