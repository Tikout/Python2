def Dodawanie(x = int, y = int) -> int:
    '''Dodaje liczby i zwraca sume'''
    return "Wynik", + x + y

def Odejmowanie(x = int, y = int) -> int:
    '''Odejmuje liczbe 1 od liczby 2  i zwraca roznice'''
    return "Wynik", + x - y

def Mnozenie(x = int, y = int) -> int:
    '''Mnozy przez siebie liczby i zwraca iloczyn'''
    return "Wynik", + x * y

def Dzielenie(x = int, y = int) -> int:
    '''Dzieli liczbe 1 przez liczbe 2 i zwraca iloraz'''
    return "Wynik", + x / y

print("Wybierz operacje")
print("1.Dodawanie")
print("2.Odejmowanie")
print("3.Mnozenie")
print("4.Dzielenie")

while True:
    wybor = input("Wybierz dzialanie(1/2/3/4): ")

    if wybor in ('1', '2', '3', '4'):
        try:
            liczba1 = float(input("Wpisz pierwsza liczbe: "))
            liczba2 = float(input("Wpisz druga liczbe: "))
        except ValueError:
            print("Cos jest nie tak, stosuj sie do polecen.")
            continue

        if wybor == '1':
            print(Dodawanie.__doc__)
            print(liczba1, "+", liczba2, "=", Dodawanie(liczba1, liczba2))

        elif wybor == '2':
            print(Odejmowanie.__doc__)
            print(liczba1, "-", liczba2, "=", Odejmowanie(liczba1, liczba2))

        elif wybor == '3':
            print(Mnozenie.__doc__)
            print(liczba1, "*", liczba2, "=", Mnozenie(liczba1, liczba2))

        elif wybor == '4':
            print(Dzielenie.__doc__)
            print(liczba1, "/", liczba2, "=", Dzielenie(liczba1, liczba2))
        
        Nowe_dzialanie = input("Nowe dzialanie ? (Tak/Nie): ")
        if Nowe_dzialanie == "Nie" or "nie":
          break
    else:
        print("Cos jest nie tak")