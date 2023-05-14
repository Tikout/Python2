from random import randint

liczba = randint(0,100)
odp = -1 
proby = 0

while odp != liczba:
    odp += 1 
    odp =int(input("Odgadnij liczbe: "))
    if odp < liczba:
        print("Liczba jaka podales jest mniejsza od wylosowanej !")
    elif odp > liczba:
        print("Liczba jaka podales jest wieksza od wylosowanej !")
print("Brawo ! Odgadles za",proby,"razem.")