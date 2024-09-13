import unittest

# Функция для определения позиции точки (x, y) относительно прямоугольника с размерами g и h
def position_get(x, y, g, h):
    try:
        # Преобразование входных значений в целые числа
        x = int(x)
        y = int(y)
        g = int(g)
        h = int(h)

        # Если координаты отрицательные, устанавливаем их в 1
        if x < 0:
            x = 1
        if y < 0:
            y = 1
        if g < 0:
            g = 1
        if h < 0:
            h = 1

        # Проверка положения точки относительно центра прямоугольника
        if y == g / 2:
            if x == h / 2:
                return "центр"  # Точка в центре
            elif x == h:
                return "правая сторона"  # Точка на правой стороне
            elif x == 0:
                return "левая сторона"  # Точка на левой стороне
            elif x < h / 2:
                return "левее от центра"  # Точка левее центра
            elif x > h / 2:
                return "правее от центра"  # Точка правее центра
        elif x == h / 2:
            if y == g:
                return "нижняя сторона"  # Точка на нижней стороне
            elif y == 0:
                return "верхняя сторона"  # Точка на верхней стороне
            elif y < g / 2:
                return "выше от центра"  # Точка выше центра
            elif y > g / 2:
                return "ниже от центра"  # Точка ниже центра
        elif y < g / 2:
            if x < h / 2:
                return "верхняя левая сторона"  # Верхняя левая часть
            else:
                return "верхняя правая сторона"  # Верхняя правая часть
        else:
            if x < h / 2:
                return "нижняя левая сторона"  # Нижняя левая часть
            else:
                return "нижняя правая сторона"  # Нижняя правая часть
    except:
        return "не корректный ввод данных"  # Обработка ошибок ввода

# Класс для тестирования функции position_get
class test_position(unittest.TestCase):
    def test_position_is_storona(self):
        # Проверка позиций на границах прямоугольника
        lst = ["левая сторона", "правая сторона", "верхняя сторона", "нижняя сторона"]
        self.assertEqual(lst[0], position_get(0, 2, 4, 4))  # Левая сторона
        self.assertEqual(lst[1], position_get(4, 2, 4, 4))  # Правая сторона
        self.assertEqual(lst[2], position_get(2, 0, 4, 4))  # Верхняя сторона
        self.assertEqual(lst[3], position_get(2, 4, 4, 4))  # Нижняя сторона

    def test_position_is_chast(self):
        # Проверка позиций в частях прямоугольника
        lst = ["верхняя левая сторона", "верхняя правая сторона", "нижняя левая сторона", "нижняя правая сторона"]
        self.assertEqual(lst[0], position_get(1, 1, 4, 4))  # Верхняя левая сторона
        self.assertEqual(lst[1], position_get(3, 1, 4, 4))  # Верхняя правая сторона
        self.assertEqual(lst[2], position_get(1, 3, 4, 4))  # Нижняя левая сторона
        self.assertEqual(lst[3], position_get(3, 3, 4, 4))  # Нижняя правая сторона

    def test_position_is_center(self):
        # Проверка позиции в центре и вокруг него
        lst = ["центр", "левее от центра", "правее от центра", "выше от центра", "ниже от центра"]
        self.assertEqual(lst[0], position_get(2, 2, 4, 4))  # Центр
        self.assertEqual(lst[1], position_get(1, 2, 4, 4))  # Левее от центра
        self.assertEqual(lst[2], position_get(3, 2, 4, 4))  # Правее от центра
        self.assertEqual(lst[3], position_get(2, 1, 4, 4))  # Выше от центра
        self.assertEqual(lst[4], position_get(2, 3, 4, 4))  # Ниже от центра

    def test_str_a_digit(self):
        # Проверка на ввод строк, которые могут быть преобразованы в числа
        self.assertEqual("центр", position_get("2", "2", "4", "4"))

    def test_str_alfa(self):
        # Проверка на ввод недопустимых строк
        self.assertEqual("не корректный ввод данных", position_get("ffsa", "ffsa", "sda", "sda"))

    def test_position_zero_x_y(self):
        # Проверка на отрицательные значения координат
        self.assertEqual("верхняя левая сторона", position_get(-1, -41, 10, 10))