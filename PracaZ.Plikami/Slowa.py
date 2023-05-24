from os import path
import os

dir_path = path.dirname(__file__)
filename = "tekst.txt"
data_path1 = path.join(dir_path, filename)
if not os.path.exists(data_path1):
    print("Brak pliku z tekstem")
    exit()
with open(data_path1, 'r', encoding= 'Utf-8') as file:
    dane = file.read()
    slowa = dane.split()

    print('Tyle jest slow w pliku :', len(slowa))