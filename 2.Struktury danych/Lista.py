list = ["burak", "cukinia", "pomidor", "cytryna", "ananas", "papryka", "dynia"]
nowalista = []
uzytkownik = input("Podaj prosze pierwsza litere")

for x in list:
    if uzytkownik in list[:0]:
        nowalista.append(x)

print(nowalista)