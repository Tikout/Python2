class Czytelnik:
    def __init__(self,imie,nazwisko,wiek,adres):
        self.imie = imie
        self._nazwisko = nazwisko
        self._wiek = wiek
        self.lista_adresow = ["Urzednicza 4/3", "Mariacka 4/2"]
        self.__update(adres)

    def update(self, adres):
        for item in adres:
            self.lista_adresow.append(item)

    __update = update
class MappingSubclass(Czytelnik):

    def update(self, keys, values):
        for item in zip(keys, values):
            self.items_list.append(item)



def pobierz_wiek(self) -> int:
    return self._wiek
def pobierz_imie(self) -> str:
    return self.imie

czytelnik1 = Czytelnik(
    imie= "Mateusz",
    nazwisko="Mąciwor",
    wiek= 21,
    adres = ""
)

czytelnik2 = Czytelnik(
    imie= "Natalia",
    nazwisko="Muszka",
    wiek= 21,
    adres = ""
)

print(pobierz_imie(czytelnik1))
print(pobierz_wiek(czytelnik1))

print(pobierz_imie(czytelnik2))
print(pobierz_wiek(czytelnik2))