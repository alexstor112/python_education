import random

number = random.randint(1, 100)
user_number = None
while number != user_number:
    user_number = int(input('Введите число: '))
    if number < user_number:
        print('Ваше число больше загаданного')
    elif number > user_number:
        print('Ваше число меньше загаданного')

print('Победа!')
