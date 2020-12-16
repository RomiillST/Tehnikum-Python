# 1+2+3+...+n = n(n+1)/2
a = 0
b = 0
n = int(input("Введите n: "))
n1 = ((n*(n+1))/2)
while a != n:
     a = a+1
     b = b +a
print( n1 == b)
print(n1)