n = int(input('укажите количество чисел: '))
numbers = input(f'введите {n} чисел через пробел: ').split()
count = 0

for num_str in numbers:
    num = int(num_str)
    if num == 0:
        count += 1

print(f'{count} - количество нулей в последовательности чисел')
