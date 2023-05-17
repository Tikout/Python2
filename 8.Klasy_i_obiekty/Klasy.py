class Czytelnik:
    def __init__(self,imie,nazwisko,wiek):
        self.imie = imie
        self._nazwisko = nazwisko
        self._wiek = wiek

def pobierz_wiek(self) -> int:
    return self._wiek
def pobierz_imie(self) -> str:
    return self.imie

czytelnik1 = Czytelnik(
    imie= "Mateusz",
    nazwisko="Mąciwor",
    wiek= 21
)

czytelnik2 = Czytelnik(
    imie= "Natalia",
    nazwisko="Muszka",
    wiek= 21
)

print(pobierz_imie(czytelnik1))
print(pobierz_wiek(czytelnik1))

print(pobierz_imie(czytelnik2))
print(pobierz_wiek(czytelnik2))