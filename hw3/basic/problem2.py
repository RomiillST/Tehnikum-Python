# Problem 2
a = []
b = 1
i = 1
while b != 0:
     print("Введите ", i, "-е число. ( Для завершения ввода введите 0 ) ")
     b = int(input())
     a.append(b)
     i+=1
print("Сумма чисел массива 'a' = ", sum(a))