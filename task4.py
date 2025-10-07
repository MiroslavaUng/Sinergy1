num = input('введите пятизначное целое число: ')
step1 = int(num[-2]) ** int(num[-1])
step2 = step1 * int(num[-3])
step3 = step2 / (int(num[0]) - int(num[1]))

print(f'в результате получилось число {step3}')