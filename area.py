from math import pi as PI, sqrt
import os

class Region:
    """docstring for Region"""
    def __init__(self, filename):
        super(Region, self).__init__()
        self._filename = filename
        if not os.path.exists(self._filename):
            raise FileNotFoundError(f'"{self._filename}" is not exists')
        elif not os.path.isfile(self._filename):
            raise FileNotFoundError(f'"{self._filename}" is not a file')

    def area():
        ...

    def top5():
        ...

    def figures(self):
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
    """docstring for Figure"""
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
    """"""
    def __init__(self, args):
        super().__init__(args, fig_type='Circle')

    def _area(self):
        r, = [float(elem) for elem in self.args]
        self.area = round(PI * r**2)

    def __str__(self):
        return '{}: радиус={}, площадь: {}'.format(self.fig_type, self.args, self.area)

    def __repr__(self):
        return 'Figure({})'.format(repr(self.fig_type))

class Triangle(Figure):
    """"""
    def __init__(self, args):
        super().__init__(args, fig_type='Triangle')

    def _area(self):
        a, b, c = [float(elem) for elem in self.args]
        p = (a + b + c) / 2
        self.area = round(sqrt(p * (p-a) * (p-b) * (p-c)))

class Rectangle(Figure):
    """"""
    def __init__(self, args):
        super().__init__(args, fig_type='Rectangle')

    def _area(self):
        a, b = [float(elem) for elem in self.args]
        self.area = round(a * b)


reg = Region('figures.txt')

list_fig = list(reg.figures())
print(list_fig)

for elem in reg.figures():
    print(elem)

# print(Figure.area)

# with open('figures.txt', 'r') as f:
#     figure = iter(f.readlines())

# while True:
#     print(next(figure).strip())
