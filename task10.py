a = int(input('введите целое число А: '))
b = int(input('введите целое число B >= A: '))
result = []
for i in range(a,b+1):
    if i % 2 == 0:
        result.append(i)
print(*result)


