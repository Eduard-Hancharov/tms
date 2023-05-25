name = input('Введите ваше имя:')
age = input('Введите ваш возраст:')
def greeting(age,name):
    if age <=0:
        print(f'Ошибка повторите ввод')
    elif age < 10:
        print(f'Привет, шкет {name}')
    elif age <= 18:
        print(f'Как жизнь {name}?')
    elif age < 100:
        print(f'Чего желаете {name}?')
    else:
        print(f'{name}, вы лжёте - в наше время столько не живут...')
greeting(int(age),name)

while True:
 name = input('Введите ваше имя:')
 age = input('Введите ваш возраст:')
 greeting(int(age),name)