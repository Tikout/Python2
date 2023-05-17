from os import path
import os



nazwiska = open("nazwiska.txt", "r")

Nazwiskaa = nazwiska.read()

lista_nazwisk = [nazwiska]

imiona = open("imiona.txt", "r")

Imiona = imiona.read()

lista_imion = [imiona]

ilosc = input(int("Ile razy wyprintowac ?"))

for imie in lista_imion:
    for nazwisko in lista_nazwisk:
        for i in range(ilosc):
            print(imie + nazwisko)