import random

# создаем матрицу со случайными числами
def create_random_matrix(rows, cols, min_val, max_val):
    return [
        [random.randint(min_val, max_val) for j in range(cols)]
        for i in range(rows)
    ]

# складываем две матрицы
def add_matrix(matrix1, matrix2):

    # проверка размеров матриц
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError('Матрицы должны иметь одинаковые размеры')

    # создание результирующей матрицы
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            # складываем соответствующие элементы и добавляем в строку
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)        # добавляем готовую строку в результат

    return result

# main
def main():
    print('СЛОЖЕНИЕ МАТРИЦ')

    # ввод параметров для матрицы 1
    print('\nПараметры для матрицы 1')
    rows_1 = int(input('Введите количество строк для матрицы 1: '))
    cols_1 = int(input('Введите количество столбцов для матрицы 1: '))
    min_val_1 = int(input('Введите минимальное число для матрицы 1: '))
    max_val_1 = int(input('Введите максимальное число для матрицы 1: '))

    print('\nМатрицы должны иметь одинаковые размеры')

    # ввод параметров для матрицы 2
    print('\nПараметры для матрицы 2')
    rows_2 = int(input('Введите количество строк для матрицы 2: '))
    cols_2 = int(input('Введите количество столбцов для матрицы 2: '))
    min_val_2 = int(input('Введите минимальное число для матрицы 2: '))
    max_val_2 = int(input('Введите максимальное число для матрицы 2: '))

    # создание матриц
    matrix_1 = create_random_matrix(rows_1, cols_1, min_val_1, max_val_1)
    matrix_2 = create_random_matrix(rows_2, cols_2, min_val_2, max_val_2)

    # вывод матриц
    print('Матрица 1:')
    for row in matrix_1:
        print(row)

    print('Матрица 2:')
    for row in matrix_2:
        print(row)

    # сложение матриц
    try:
        result = add_matrix(matrix_1, matrix_2)
        print('\nРезультат сложения:')
        for row in result:
            print(row)
    except ValueError as e:
        print(f'Сложение не возможно: {e}')

# запуск программы
if __name__ == '__main__':
    main()
