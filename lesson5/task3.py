list_numbers = [1, 4, 5, 4, 1, 6, 7, 8, 1, 4]
def numbers(lists):
    dictionary = {}
    for num in lists:
        dictionary[num] = dictionary.get(num, 0) + 1
    return dictionary
dictionary = numbers(list_numbers)
print(dictionary)
