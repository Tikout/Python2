class Czytelnik:
    def __init__(self, imie, nazwisko, nr_karty):
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__nr_karty = nr_karty
    def info(self):
        print(f"Czytelnik: {self.__imie} {self.__nazwisko}, nr karty: {self.__nr_karty}")


    

    
czytelnik1 = Czytelnik("Jan", "Kowalski", 12345)
czytelnik2 = Czytelnik("Anna", "Nowak", 67890)
czytelnik3 = Czytelnik("Mariusz", "Pudzianowski", 42069)
czytelnik4 = Czytelnik("Robert", "Nowak", 21370)
czytelnik5 = Czytelnik("Jakub", "Robaszewski", 66666)

def pobierz_nr_karty(self) -> int:
    return self.__nr_karty
print(pobierz_nr_karty(czytelnik1))

