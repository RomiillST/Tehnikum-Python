import time
import os

def zero():
    z = []
    s = str(input('Введите ряд чисел( через пробел ): '))
    s = s.split(' ')
    l = len(s)
    for x in s:
        if x == '0':
            z.append(x)
            s.remove(x)
    z = s + z
    print(z)

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
        while True:
            s = str(input('Введите вашу строку: '))
            if s == "0" :
                print('Спасибо за пользование моими функциями Нуриддин!')
                break
            count = 1
            el = s[0]
            for i in s[1:]:
                if el[-1] == i:
                    count += 1
                else:
                    el += str(count) + i
                    count = 1
            el += str(count)
            print(el)
            print("Для завершения работы - введите 0")           
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
