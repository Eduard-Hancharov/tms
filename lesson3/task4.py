number = int(input('Введите цифру'))
sum = 0
for i in range(1,number+1):
    sum +=i**3
print(sum)



number = int(input('Введите цифру'))
sum = 0
i = 1
while i<=number:
    sum +=i**3
    i += 1
print(sum)