plik = open("C:\Python-Part2\Praca z plikami\tekst.txt", "rt")
dane = plik.read()
slowa = dane.split()

print('Tyle jest slow w pliku :', len(slowa))