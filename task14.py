n = int(input('введите количество чисел: '))

if n < 1 or n > 100000:
    print('нужно ввести число, чтобы 1 ≤ N ≤ 100 000')
    exit()

numbers = list(map(int,input('введите числа через пробел: ').split()))

if len(numbers) != n:
    print(f'введено {len(numbers)} вместо чисед {n}')
    exit()

for j in numbers:
    if j < 1 or j > 10**9:
        print('нужно ввести число, чтобы 1 ≤ Ai ≤ 10e9')
        exit()

result = []
result.append(numbers[-1])
for i in range(n-1):
    result.append(numbers[i])

print(*result)
