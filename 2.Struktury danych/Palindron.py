a = (input("Podaj słowo"))

a_odwrocone = a[::-1]

if a_odwrocone == a:
    print("Palindron")
else:
    print("Nie Palindron")