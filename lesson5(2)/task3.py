words = ("mom", "Mother", "dad", "Father")
result = list(filter(lambda a:a == a[::-1], words))
print(result)