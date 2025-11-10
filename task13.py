n = int(input('введите количество чисел N: '))

if n < 1 or n > 10000:
    print(f'N должно быть от 1 до 10000, введено {n}')
    exit()

numbers = []
for i in range(n):
    num = int(input('введите число: '))

    if abs(num) > 10**5:
        print(f'число {num} превышает допустимое значение 100000 ')
        exit()

    numbers.append(num)

reversed_numbers = numbers[::-1]
for num in reversed_numbers:
    print(num)