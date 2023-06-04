def count_words_and_letter_statistics(file_path):
    letter_stats = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.split()
            for word in words:
                last_letter = word[-1].lower()
                if not last_letter.isalpha():
                    last_letter = word[-2].lower() if len(word) > 1 else ''
                if last_letter in letter_stats:
                    letter_stats[last_letter] += 1
                else:
                    letter_stats[last_letter] = 1
    total_words = sum(letter_stats.values())
    print(f"Total words: {total_words}")
    for letter, count in letter_stats.items():
        print(f"Words ending with '{letter}': {count}")

count_words_and_letter_statistics('C:\Users\Kuba\Desktop\Python-Part2\PracaZ.Plikami\tekst.txt')