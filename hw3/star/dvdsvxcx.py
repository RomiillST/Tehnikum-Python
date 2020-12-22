s = input()
count = 1
result = ""

for i in range(len(s)-1):
    if s[i] == s[i+1]:
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
