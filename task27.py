class Cash:

    def __init__(self, summa):
        self.summa = summa

    def top_up(self, x):
        self.summa += x    # увеличиваем баланс
        return self.summa  # возвращаем новый баланс

    def count_1000(self):
        return self.summa // 1000  # целочисленное деление

    def take_away(self, x):
        if x > self.summa:
            return f'Недостаточно денег. Текущий аланс {self.summa}'
        self.summa -= x
        return self.summa


# создание объекта
a = Cash(10000)

# использование методов
print(a.top_up(5000))
print(a.count_1000())
print(a.take_away(20000))
print(a.take_away(5000))