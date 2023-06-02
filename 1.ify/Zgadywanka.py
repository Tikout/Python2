from random import randint

liczba = randint(0,100)
odp = -1
proby = 0

while odp != liczba:
    proby += 1 
    odp =int(input("Odgadnij liczbe: "))
    if odp < liczba:
        print("Liczba jaka podales jest mniejsza od wylosowanej !")
    elif odp > liczba:
        print("Liczba jaka podales jest wieksza od wylosowanej !")
    
    if odp == liczba:
        print("Brawo ! Odgadles po",proby,"razach !.")

        Nowe_dzialanie = input("Gramy znowu ? (Tak/Nie): ")
        if Nowe_dzialanie == "Nie" or "nie":
            break

else:
        print("Cos jest nie tak")