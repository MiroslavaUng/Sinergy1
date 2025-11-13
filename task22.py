import collections

# база данных
pets = {}

# получение информации о питомце по ID
def get_pet(ID):
    return pets[ID] if ID in pets.keys() else False

# склонение возраста
def get_suffix(age):
    if 11 <= age % 100 <= 14:
        return 'лет'
    elif age % 10 == 1:
        return 'год'
    elif 2 <= age % 10 <= 4:
        return 'года'
    else:
        return 'лет'

# отображение всех питомцев
def pets_list():
    if not pets:
        print('В базе данных нет питомцев')
        return

    for ID, pet_info in pets.items():
        for name, info in pet_info.items():
            age = info["Возраст питомца"]
            age_suff = get_suffix(age)
            print(f'ID: {ID}. Это {info["Вид питомца"]} по кличке "{name}".' 
                  f' Возраст питомца: {age} {age_suff}.' 
                  f' Имя владельца: {info["Имя владельца"]}')

# создание новой записи с информацией о питомце
def create():

    if pets:
        last = collections.deque(pets, maxlen=1)[0]
        new_id = last + 1
    else:
        new_id = 1

    name = input('Введите имя питомца: ')
    pet_type = input('Введите вид питомца: ')
    age = int(input('Введите возраст питомца: '))
    owner = input('Введите имя владельца: ')

    pets[new_id] = {
        name: {
            'Вид питомца': pet_type,
            'Возраст питомца': age,
            'Имя владельца': owner
        }
    }

    print(f'Питомец успешно добавлен с ID: {new_id}')

# чтение информации о питомце по ID
def read(ID):
    pet_info = get_pet(ID)
    if not pet_info:
        print(f'Питомец с ID {ID} не найден')
        return

    for name, info in pet_info.items():
        age = info["Возраст питомца"]
        age_suff = get_suffix(age)
        print(f'ID: {ID}. Это {info["Вид питомца"]} по кличке "{name}".' 
              f' Возраст питомца: {age} {age_suff}.' 
              f' Имя владельца: {info["Имя владельца"]}')

# обновление информации о питомце по ID
def update(ID):
    pet_info = get_pet(ID)
    if not pet_info:
        print(f'Питомец с ID {ID} не найден.')
        return

    # получаем текущее имя питомца
    current_name = list(pet_info.keys())[0]
    current_info = pet_info[current_name]

    print(f' Введите новые данные.'
          f' Если поле не нужно менять, нажмите Enter.')

    new_name = input('Введите новое имя питомца: ') or current_name
    new_type = input('Введите новый вид питомца: ') or current_info["Вид питомца"]

    age_input = input(f'Введите новый возраст питомца: ')
    new_age = int(age_input) if age_input else current_info["Возраст питомца"]

    new_owner = input('Введите новое имя владельца: ') or current_info["Имя владельца"]

    # обновляем запись
    pets[ID] = {
        new_name: {
            'Вид питомца': new_type,
            'Возраст питомца': new_age,
            'Имя владельца': new_owner
        }
    }
    print(f'Информация о питомце с ID: {ID} успешна обновлена.')

# удаление питомца по ID
def delete(ID):
    if ID in pets:
        pet_name = list(pets[ID].keys())[0]
        del pets[ID]
        print(f'Питомец {pet_name} c ID {ID} успешно удален')
    else:
        print(f'Питомец с ID {ID} не найден')

# main
def main():
    while True:
        print("\n=== Ветеринарная клиника ===")
        print("1. Создать нового питомца")
        print("2. Просмотреть информацию о питомце")
        print("3. Обновить данные о питомце")
        print("4. Удалить питомца из базы данных")
        print("5. Показать всех питомцев")
        print("stop. Выйти из системы")

        command = input('\nВыберите действие: ').strip().lower()

        if command == 'stop':
            print('Выход из системы')
            break

        elif command == '1':
            create()

        elif command == '2':
            try:
                ID = int(input('Введите идентификатор питомца: '))
                read(ID)
            except ValueError:
                print('Ошибка: введите числовой идентификатор')

        elif command == '3':
            try:
                ID = int(input('Введите идентификатор питомца: '))
                update(ID)
            except ValueError:
                print('Ошибка: введите числовой идентификатор')

        elif command == '4':
            try:
                ID = int(input('Введите идентификатор питомца: '))
                delete(ID)
            except ValueError:
                print('Ошибка: введите числовой идентификатор')

        elif command == '5':
            pets_list()
        else:
            print('Неизвестная команда. Попробуйте снова')

# запуск
if __name__ == "__main__":
    main()