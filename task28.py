class Turtle:

    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s

    # увеличивает y на s (вверх)
    def go_up (self):
        self.y += self.s
        return self.y

    # уменьшает y на s (вниз)
    def go_down (self):
        self.y -= self.s
        return self.y

    # уменьшает x на s (влево)
    def go_left(self):
        self.x -= self.s
        return self.x

    # увеличивает x на s (вправо)
    def go_right(self):
        self.x += self.s
        return self.x

    # увеличивает s на 1 (скорость увеличивается)
    def evolve(self):
        self.s += 1
        return self.s

    # уменьшает s на 1 или выкидывает ошибку, когда s может стать ≤ 0 (скорость уменьшается)
    def degrade(self):
        if self.s <= 1:
            raise ValueError ('Действие не возможно')
        self.s -= 1
        return self.s


    # возвращает минимальное количество действий, за которое черепашка сможет добраться до x2 y2 от текущей позиции
    def count_moves(self, x2, y2):
        # вычисляем абсолютную разницу по координатам (важно только расстояние до цели, а не направление)
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)

        # вычисляем количество шагов по каждой координате (округление вверх)
        step_x = (dx + self.s - 1) // self.s
        step_y = (dy + self.s - 1) // self.s

        # минимальное количество действий
        min_step = step_x + step_y
        return min_step

# создание объекта
a = Turtle(10,20,5)

# вызов методов
print('Текущая позиция: ', (a.x, a.y))
print('Вверх: ', a.go_up())
print('Вниз: ', a.go_down())
print('Влево: ', a.go_left())
print('Вправо: ', a.go_right())
print('Увеличиваем шаг: ', a.evolve())
print('Уменьшаем шаг: ', a.degrade())

print('Минимальное количество действий до (30, 50): ', a.count_moves(30,50))