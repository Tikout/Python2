wiek = input("Podaj wiek")
wiekk = int(wiek)

kategoria = input("Jaką masz kategorię prawa jazdy")

ile = input("Przez ile masz prawo jazdy")

if (wiekk >= 24) or (kategoria == "A2" and ile >= 2):
    print ("Użytkownik może przystąpić do egzaminu")
else:
    print ("Nie może przystąpić do egzaminu")
