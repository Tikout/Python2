class Czlowiek:
  def __init__(self, imie, nazwisko):
    self.imie = imie
    self.nazwisko = nazwisko

  def printname(self):
    print(self.imie, self.nazwisko)


x = Czlowiek("Maciej","Laskowski" )
x.printname()