import os
import string

def count_words(text):
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    word_count = len(words)
    return word_count

def word_ending_stats(text):
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    ending_stats = {}

    for word in words:
        if word:
            last_letter = word[-1].lower()
            if last_letter in ending_stats:
                ending_stats[last_letter] += 1
            else:
                ending_stats[last_letter] = 1
    return ending_stats

filename = "tekst.txt"
current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, filename)

with open(file_path, "r", encoding="utf-8") as f:
    file_text = f.read()

word_count = count_words(file_text)
print("Liczba słów:", word_count)

ending_stats = word_ending_stats(file_text)
print("Statystyki końcówek słów:")
for letter, count in ending_stats.items():
    print(f"Litera '{letter}': {count} słów")
