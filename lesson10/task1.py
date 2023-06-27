number1 = float(input("Введите первое число: "))
operation = input("Введите операцию: ")
number2 = float(input("Введите второе число: "))
if operation == '+':
    print(number1 + number2)
elif operation == '-':
    print(number1 - number2)
elif operation == '/':
    print(number1 / number2)
elif operation == '*':
    print(number1 * number2)
else:
    print("Ошибка")
