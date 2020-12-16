asf = str(input())
x = []
i = len(asf)
b = 1
while b != i+1:
     x.append(asf[i-b])
     b+=1
print(x)