word1 = 'Пайтон'
word2 = 'Питон'
print(word1 + ' ' + word2)
word1, word2 = word2, word1
print('!' + word1 + ' ' + '!' + ' ' + word2 + '!')
print(f"!{word1} ! {word2}!")
print('!{0} ! {1}!'.format(word1, word2))


