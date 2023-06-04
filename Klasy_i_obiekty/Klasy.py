class Czytelnik:
    def init(self, imie, nazwisko, numer_id):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_id = numer_id

    def str(self):
        return f"Czytelnik {self.imie} {self.nazwisko}, ID: {self.numer_id}"
czytelnik1 = Czytelnik("Jan", "Kowalski", "123")
czytelnik2 = Czytelnik("Anna", "Nowak", "456")

print(czytelnik1)
print(czytelnik2)