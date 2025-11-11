num_list = list(map(int, input('Введите последовательность чисел через пробел: ').split()))
seen = set()

for i in num_list:
    if i in seen:
        print('YES - это число ранее встречалось')
    else:
        print('NO - это число ранее не встречалось')
        seen.add(i)