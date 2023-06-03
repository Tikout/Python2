def Dodawanie(x, y):
    return x + y

def Odejmowanie(x, y):
    return x - y

def Mnozenie(x, y):
    return x * y

def Dzielenie(x, y):
    return x / y
    

print("Wybierz operacje")
print("1.Dodawanie")
print("2.Odejmowanie")
print("3.Mnozenie")
print("4.Dzielenie")

def Kalkulator():
    while True:
        wybor = input("Wybierz dzialanie(1/2/3/4): ")

        if wybor in ('1', '2', '3', '4'):
            try:
                liczba1 = float(input("Wpisz pierwsza liczbe: "))
                liczba2 = float(input("Wpisz druga liczbe: "))
            except ValueError as ERROR:
                print("Cos jest nie tak, stosuj sie do polecen.")
                print(ERROR)
                print("Sprobuj jeszcze raz")
                continue

            if wybor == '1':
                print(liczba1, "+", liczba2, "=", Dodawanie(liczba1, liczba2))

            elif wybor == '2':
                print(liczba1, "-", liczba2, "=", Odejmowanie(liczba1, liczba2))

            elif wybor == '3':
                print(liczba1, "*", liczba2, "=", Mnozenie(liczba1, liczba2))

            elif wybor == '4':
                if liczba2 == 0:
                    print("Błąd ! Nie można dzielić prez 0 !")
                else:
                    print(liczba1, "/", liczba2, "=", Dzielenie(liczba1, liczba2))

# Po usunięciu lub zakomentowaniu Nowe_Dzialanie program przestaje działać dobrze

            Nowe_dzialanie = ("Nowe dzialanie ? (Tak/Nie): ")
            if Nowe_dzialanie == "Nie" or "nie":
                break
            elif Nowe_dzialanie == "Tak" or "tak":
                Kalkulator()

def menu():
   while True:
       print('(1) Użyj kalkulatora')
       print('(Q) Wyjdz')
       choice = input('Co chcesz zrobić ?: ').lower()
       if choice == '1':
           Kalkulator()
       elif choice == 'q':
           return False
       else:
           print(f'Cos jest nie tak: {choice}')

if __name__ == '__main__':
    menu()