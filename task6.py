word = input('введите слово из маленьких латинских букв: ')
vowels = 'aeiou'

# общее количество гласных и согласных в слове
vowels_count = 0
consonants_count = 0

for char in word:
    if char in vowels:
        vowels_count += 1
    else:
        consonants_count +=1

print(f'общее количество гласных {vowels_count}')
print(f'общее количество согласных {consonants_count}')

# считаем количество каждой гласной буквы из перечня в слове
print('количество каждой гласной буквы:')
for vowel in vowels:
    count = word.count(vowel)
    print(f'буква "{vowel}": {count}')
    if count == 0:
       print(f'False - буквы {vowel} нет в слове')