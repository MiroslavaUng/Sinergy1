m = int(input("Введите грузоподъемность лодки (1-1000000): "))
n = int(input("Введите количество рыбаков (1-100): "))

if m < 1 or m > 10**6:
    print("Ошибка: грузоподъемность должна быть от 1 до 1000000")
    exit()

if n < 1 or n > 100:
    print("Ошибка: количество рыбаков должно быть от 1 до 100")
    exit()

weights = []
for i in range(n):
    weight = int(input(f'введите вес рыбака {i+1}: '))
    if weight < 1 or weight > m:
        print(f'вес должен быть от 1 до {m}')
        exit()
    weights.append(weight)

#сортируем веса по возрастанию
weights.sort()

boats = 0
small = 0
big = n - 1

while small <= big:
    # если самый тяжелый и самый легкий могут пойти вместе
    if small != big and weights[small] + weights[big] <= m:
        small += 1  # самого легкого сажаем с самым тяжелым
    # иначе самый тяжелый плывет один
    big -= 1
    boats += 1

print(f'минимальное количество лодок: {boats}')
