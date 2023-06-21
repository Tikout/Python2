import random
import os

def load_names_from_file(file_path):
    names = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            name = line.strip()
            if name:
                names.append(name)
    return names

def generate_combinations(first_names, last_names, num_combinations):
    combinations = set()

    while len(combinations) < num_combinations:
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        combination = f"{first_name} {last_name}"
        combinations.add(combination)

    return combinations

num_combinations = int(input("Podaj liczbę kombinacji do wygenerowania: "))

current_directory = os.path.dirname(os.path.abspath(__file__))
first_names_file = os.path.join(current_directory, "imiona.txt")
last_names_file = os.path.join(current_directory, "nazwiska.txt")

first_names = load_names_from_file(first_names_file)
last_names = load_names_from_file(last_names_file)

combinations = generate_combinations(first_names, last_names, num_combinations)

file_path = os.path.join(current_directory, "kombinacje_imion_nazwisk.txt")
with open(file_path, "w", encoding="utf-8") as file:
    for combination in combinations:
        file.write(combination + "\n")

print(f"Generowanie kombinacji zakończone. Zapisano do pliku {file_path}.")
