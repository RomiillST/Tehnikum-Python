
import time
import os

def stroka():
    while True:
        s = input()
        count = 1
        result = ""
        if s == '0':
            break
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                count += 1
            else:
                if count != 1:
                    result += s[i] + str(count)
                else:
                    result += s[i]
                count = 1
        if count != 1:
            result += s[-1] + str(count)
        else:
            result += s[-1]
        print(result)

def zero():
    while True:
        z = []
        s = str(input('Введите ряд чисел( через пробел ): '))
        if s == '*':
            break
        s = s.split(' ')
        l = len(s)
        for x in s:
            if x == '0':
                z.append(x)
                s.remove(x)
        z = s + z
        print(z)
        print('Для завершения работы архиватора - введите *.')

def load():
    os.system('cls')
    print('L')
    time.sleep(0.3)
    os.system('cls')
    print('L O')
    time.sleep(0.3)
    os.system('cls')
    print('L O A')
    time.sleep(0.3)
    os.system('cls')
    print('L O A D')
    time.sleep(0.3)
    os.system('cls')
    print('L O A D I')
    time.sleep(0.3)
    os.system('cls')
    print('L O A D I N')
    time.sleep(0.3)
    os.system('cls')
    print('L O A D I N G')
    time.sleep(0.3)
    os.system('cls')
    print('L O A D I N G .')
    time.sleep(0.3)
    os.system('cls')
    print('L O A D I N G . .')
    time.sleep(0.3)
    os.system('cls')
    print('L O A D I N G . . .')
    time.sleep(0.3)
    os.system('cls')


print('''Привет. Я бот для ленивого Нуридина. Для того, чтобы проверить - Нуриддин ли вы - закончите вашу великую цитату: Лучшая домашка - это ...
1. сделанная вовремя домашка
2. та, которую оценил Махмуд ака
3. не заданная домашка
''')
answ = int(input('Мой ответ: '))
if answ == 3:
    os.system('cls')
    print('Добро пожаловать мой господин. Чего желаете?')
    print('''
    1. Сжать строку, чтобы места меньше занимала.
    2. Проредить массив чисел, уж больно много там нулей.
    0. Я незнаю чего я хочу.
    ''')
    answ = int(input('Выбираю: '))

    if answ == 1:
        load()
        print('Приступаем!')
        s = 0
        stroka()
    elif answ == 2:
        os.system('cls')
        load()
        zero()
        print('Спасибо за пользование моими функциями Нуриддин!')
    else:
        time.sleep(2)
        os.system('cls')
        print('''
       ▀   █ █ █▀▀▄ ▄▀▀▄ █   █
       █   █▀▄ █  █ █  █ █▄█▄█
       ▀   ▀ ▀ ▀  ▀  ▀▀   ▀ ▀
    ▀█▀ █ █ ▄▀▄ ▀█▀  █▀ █▀ █▀ █   █▀▄ █▀▄ ▄▀▄
     █  █▀█ █▄█  █   █▀ █▀ █▀ █   █▀▄ █▄▀ █ █
     ▀  ▀ ▀ ▀ ▀  ▀   ▀  ▀▀ ▀▀ ▀▀  ▀▀  ▀ ▀  ▀   
                          ▄█▀▀▀▀▀█▄
                ▄▄▄▄▄   █▀        ▀█
               █    ▀█▄█           ▀█
             ██       █      ▄▄      █
            █          █ ▄▄▀▀  ▀▀▀▀   █
           █           █    ▀▀▄▄▄▀▀   █
          ▐             █             █
          ▐             █ ▀▀▀▄    ▄   █
          ▐             █     ▀  ▀ ▀▄ █
          ▐             █ ███▄        █
          ▐             █    ▀    ██ ▐
          ▐             █       ▄     █▄▄
          ▐             █         ▌   ██ ▌
          ▐             █   ▄▀ ▄ ▌   █   ▌
           █            █    ▀  ▀   █    ▌
            █            █   ▄▄▄▄  █     ▌
          ▄▀▀▄   ▌       ██       █▌     ▌
        ▄▀    █  ▌        ▀▀█████▀▀      ▌
      ▄▀       ███▌         ▌            ▌
    ▄▀            █                     █
    █       ▄██▀▀▀▀                     ▌
    █     ▄██▄                          ▌
    █        ▀▄      ▄▀▀▀▀▄            █
    █          ▀▄  ▄▀  ▄▄▄▀            ▌
    ▀▄           ▀▀    █               ▌
    █ ▀▄                ▀▀▀▀▀▄         ▌
    █   ▀▄▄               ▄▄▄▀         ▌''')
else:
    os.system('cls')
    print("Мдааа... Не для вас мои коды писались. Брысь!")
