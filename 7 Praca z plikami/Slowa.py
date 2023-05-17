file = open("C:\Python-Part2\Praca z plikami\tekst.txt", "rt")
data = file.read()
words = data.split()

print('Number of words in text file :', len(words))