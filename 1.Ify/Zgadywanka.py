from random import randint
while True:
    liczba = randint(0, 100)
    proba = 0

    while True:
        odp = int(input("Podaj liczbę!: "))
        proba += 1
        if odp == liczba:
            print(f"Gratulacje! Odgadłeś liczbę {liczba} w {proba} strzałach.")
            break
        elif odp < liczba:
            print("Liczba jest większa.")
        else:
            print("Liczba jest mniejsza.")

    dalej = input("Chcesz grać dalej? (tak/nie): ")
    if dalej.lower() != "tak":
        break

