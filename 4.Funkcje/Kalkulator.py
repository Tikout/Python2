while True:
    print('Kalkulator')
    print('1. dodawanie')
    print('2. odejmowanie')
    print('3. mnożenie')
    print('4. dzielenie')
    print('5. wyjście')
    dzialanie = input("Podaj działanie: ")
    if dzialanie == '1':  
      a = int(input('Podaj pierwszą liczbę: '))
      b = int(input('Podaj drugą liczbę: '))
      wynik = a + b
    elif dzialanie == '2':
      a = int(input('Podaj pierwszą liczbę: '))
      b = int(input('Podaj drugą liczbę: '))
      wynik = a - b
    elif dzialanie == '3':
      a = int(input('Podaj pierwszą liczbę: '))
      b = int(input('Podaj drugą liczbę: '))
      wynik = a * b
    elif dzialanie == '4':
      a = int(input('Podaj pierwszą liczbę: '))
      b = int(input('Podaj drugą liczbę: '))
      wynik = a / b
    elif dzialanie == '5':
        break  
    else:
        wynik = 'Nie ma takiego działania'

    print("Wynik:", wynik)
    print()  
