x = int(input('введите натуральное число до 2 миллиард: '))
if x < 1 or x > 2e9:
    print('некорректно введено число, должно быть от 1 до 2 миллиард')
else:
    count = 0

    for i in range (1, int(x**0.5) + 1):
        if x % i == 0:
            count += 1
            if i != x//i:
                count += 1
    print(f'количество делителей: {count}')
