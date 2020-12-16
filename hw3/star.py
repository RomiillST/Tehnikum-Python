import random
import time
a = 0
print('''
   ▕▔▔╲╱▔▔▔╲╱▔▔▏
    ╲＿╱    ╲＿╱
    ╱▏ ▉   ▉ ▕ 
   ╱▔╲       ╱╲
  ▏╰ ╰ ▕ ╰┳╯ ▏╯ ▏
  ▏╰ ╰  ╲╰┻╯╱ ╯ ▏
  ▏╰ ╰ ╰ ▔▔▔ ╯ ╯▏
   ╲╰┳┳ ╰ ╯ ┳┳╱
    ┃ ┳┫┣━┳┳┫┃
    ┃ ┃┃ ┃┃┃┃┃
    ┗┛┗┛ ┗┛ ┗┛
''')
print("Привет Боба! Это я - твой друг Биба. Давай играть в игру! Я загадаю число, а ты угадай его!")
time.sleep(3)
n = random.randint(0,100)
print('Загадал !')
while True:
     print()
     a = int(input('Мой ответ это: '))
     if a > n:
          print("Моё число поменьше")
          print()
     if a < n:
          print("Моё число побольше")
     if (a == n+1) or (a == n-1):
          print('КИПЯТОК!!!')
     elif (a == n+3) or (a == n+2) or (a == n-3) or (a == n-2):
          print('Горячо')
     elif (a == n+4) or (a == n+5) or (a == n-4) or (a == n-5):
          print('Тепло')
     elif a == n:
          break
     else:
          print("Холодно ")
time.sleep(2)
print()
print('Хм... А ты хорош братан!')
print("К нам на днях Пупа и Лупа заедут, так что возьми что нибудь к чаю. ")
