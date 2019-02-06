from math import pi as PI, sqrt

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
                        r = line.strip().split(',')[1]
                        fig = Circle(r)
                        yield fig
                    elif 'Triangle' in line:
                        a, b, c = line.strip().split(',')[1:-1]
                        fig = Triangle(a, b, c)
                        yield fig
                    elif 'Rect' in elem:
                        a, b = line.strip().split(',')[1:-1]
                        fig = Rectangle(a, b)
                        yield fig
        except FileNotFoundError:
            return ''
        except PermissionError:
            return ''
    
    def __iter__(self):
        return self.figures()

class Figure:
    """docstring for Figure"""
    def __init__(self, fig_type):
        super().__init__(fig_type)
        self.fig_type = fig_type
        
class Circle(Figure):
    """"""
    def __init__(self, fig_type='Circle', radius):
        super().__init__(fig_type)
        self.radius = radius

class Triangle(Figure):
    """"""
    def __init__(self, fig_type='Circle', radius):
        super().__init__(fig_type)
        self.radius = radius

class Rectangle(Figure):
    """"""
    def __init__(self, fig_type='Circle', radius):
        super().__init__(fig_type)
        self.radius = radius        

with open('figures.txt', 'r') as f:
    figure = iter(f.readlines())

while True:
    print(next(figure).strip())
