my_list = list(range(1, 101))
print([x * 10 if x % 4 != 0 else x * 2 for x in list(range(1, 101)) if x % 10 == 0])
