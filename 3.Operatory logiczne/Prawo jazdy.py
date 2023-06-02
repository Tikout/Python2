wiek = int(input("Podaj wiek"))

kategoria = input("Jaką masz kategorię prawa jazdy")

ile = input("Przez ile masz prawo jazdy")

if (wiek >= 24) or (wiek >= 20, kategoria == "A2" and ile >= 2):
    print ("Użytkownik może przystąpić do egzaminu")
else:
    print ("Nie może przystąpić do egzaminu")
