import json
dictionary = {
123456: ('Mary', 18),
123457: ('Anthony', 33),
123458: ('David', 22),
123459: ('Daria', 19),
123450: ('Andrey', 20),
234567: ('Pit', 22)
}
print(dictionary[123456])
with open('dictionary.json', 'w') as file:
    json.dump(dictionary, file)

with open('dictionary.json', 'r') as file:
    dictionary = json.load(file)