import time
print('''Я программа, которая может производить любые математические функции над любыми двумя числами.
От вас потребуется ввести первое и второе число, а так же символ математической операции.''')
print()
time.sleep(6)
x=int(1)
while x!=0:
    a = int(input("Первое число: "))
    b = int(input("Второе число: "))
    m = str(input("Математический символ(+, -, *, /) : "))
    if m=='+':
        print(a+b)
        x = int(input('''Прикольно, да? Если хочешь продолжить - нажми 1, если ты всё таки имеешь совесть и дашь мне отдохнуть - нажми 0! '''))
    else:
        if m == '-':
            print(a - b)
            x = int(input('''Прикольно, да? Если хочешь продолжить - нажми 1, если ты всё таки имеешь совесть и дашь мне отдохнуть - нажми 0! '''))
        else:
            if m == '*':
                print(a * b)
                x = int(input('''Прикольно, да? Если хочешь продолжить - нажми 1, если ты всё таки имеешь совесть и дашь мне отдохнуть - нажми 0! '''))
            else:
                if m == '/':
                    print(a / b)
                    x = int(input('''Прикольно, да? Если хочешь продолжить - нажми 1, если ты всё таки имеешь совесть и дашь мне отдохнуть - нажми 0! '''))
                else:
                    print("Вы не ввели нужный математический символ. Придётся всё с самого начала вводить :(")
print("Спасибо что воспользовались моей программой! До новых встреч! ")