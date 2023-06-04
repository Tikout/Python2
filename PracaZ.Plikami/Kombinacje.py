from os import path
import os

dir_path = path.dirname(__file__)
filename = "nazwiska.txt"
filename2 = "imiona.txt"
data_path1 = path.join(dir_path, filename)
data_path2 = path.join(dir_path, filename2)
if not os.path.exists(data_path1):
    print("Brak pliku z tekstem")
    exit()
with open(data_path1, 'r', encoding= 'Utf-8') as file:
    nazwiska = file.read()
    nazwiskaa = nazwiska.split()
with open(data_path2, 'r', encoding= 'Utf-8') as file:
    imiona = file.read()
    imionaa = imiona.split()

ilosc = input(str("Ile razy wyprintowac ?"))

for imie in imiona:
    for nazwisko in nazwiska:
            print(imie + nazwisko)