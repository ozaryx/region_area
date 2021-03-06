# -*- coding: utf-8 -*-
import os
from math import pi as PI
from math import sqrt


class Region:
    """Класс области фигур"""

    def __init__(self, filename):
        super(Region, self).__init__()
        self._filename = filename
        if not os.path.exists(self._filename):
            raise FileNotFoundError(f'"{self._filename}" is not exists')
        elif not os.path.isfile(self._filename):
            raise FileNotFoundError(f'"{self._filename}" is not a file')
        self._region_area()
        self._top5()

    def _region_area(self):
        """Вычисление суммарной площади всех фигур"""
        self.area = 0
        for elem in self.figures():
            self.area += elem.area

    def _top5(self):
        """Получение 5 самых больших фигур по площади"""
        fig_list = [(elem.fig_type, elem.area) for elem in self.figures()]
        self.top5 = sorted(fig_list, key=lambda x: x[1], reverse=True)[0:6]
        # self.top5 = fig_list

    def figures(self):
        """Создание набора объектов фигур по списку"""
        try:
            with open(self._filename, 'r', encoding='utf-8') as f:
                for line in f:
                    if 'Circle' in line:
                        args = line.strip().split(',')[1:]
                        fig = Circle(args)
                        yield fig
                    elif 'Triangle' in line:
                        args = line.strip().split(',')[1:]
                        fig = Triangle(args)
                        yield fig
                    elif 'Rect' in line:
                        args = line.strip().split(',')[1:]
                        fig = Rectangle(args)
                        yield fig
        except FileNotFoundError:
            return ''
        except PermissionError:
            return ''

    def __iter__(self):
        return self.figures()


class Figure:
    """Общий класс фигур"""

    def __init__(self, args, fig_type):
        self.fig_type = fig_type
        self.args = args
        self._area()

    def _area(self):
        self.area = None

    def __str__(self):
        return '{}: стороны={}, площадь: {}'.format(self.fig_type, self.args, self.area)

    def __repr__(self):
        return 'Figure({})'.format(repr(self.fig_type))


class Circle(Figure):
    """Класс фигуры Circle"""

    def __init__(self, args):
        super().__init__(args, fig_type='Circle')

    def _area(self):
        self.r, = (float(elem) for elem in self.args)
        self.area = round(PI * self.r**2)

    def __str__(self):
        return '{}: радиус={}, площадь: {}'.format(self.fig_type, self.r, self.area)


class Triangle(Figure):
    """Класс фигуры Triangle"""

    def __init__(self, args):
        super().__init__(args, fig_type='Triangle')

    def _area(self):
        self.a, self.b, self.c = (float(elem) for elem in self.args)
        p = (self.a + self.b + self.c) / 2
        self.area = round(sqrt(p * (p-self.a) * (p-self.b) * (p-self.c)))

    def __str__(self):
        args = (self.fig_type, self.a, self.b, self.c, self.area)
        return '{}: стороны=({}, {}, {}), площадь: {}'.format(*args)


class Rectangle(Figure):
    """Класс фигуры Rectangle"""

    def __init__(self, args):
        super().__init__(args, fig_type='Rectangle')

    def _area(self):
        self.a, self.b = (float(elem) for elem in self.args)
        self.area = round(self.a * self.b)

    def __str__(self):
        args = (self.fig_type, self.a, self.b, self.area)
        return '{}: стороны=({}, {}), площадь: {}'.format(*args)


# Создание области фигур
reg = Region('./region_area/figures.txt')

# Вывод списка фигур
list_fig = list(reg.figures())
print(list_fig)

print('')

# Вывод списка свойств фигур
print('Список фигур')
for elem in reg.figures():
    print(elem)

print('')

# Вывод площади области фигур
print('Площадь всех фигур: {}\n'.format(reg.area))

# Вывод ТОП-5 фигур по площади
print('Список ТОП-5 фигур по площади')
for elem in reg.top5:
    fig, area = elem
    print('Фигура: {}, площадь: {}'.format(fig, area))
