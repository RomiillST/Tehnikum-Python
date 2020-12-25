f = open('file.txt', 'w')
x = input('Введите строку/слово: ')
y = int(input('Введите кол-во раз, сколько строка должна повториться: '))
for _ in range(y):
    f.write(str(x)+'\n')
f.close()
