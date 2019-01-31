# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
from math import sqrt


class Triangle:
    # конструктор
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.top1 = [x1, y1]
        self.top2 = [x2, y2]
        self.top3 = [x3, y3]
        self.side1 = sqrt((x1 - x2)**2 + (y1 - y2)**2)
        self.side2 = sqrt((x2 - x3)**2 + (y2 - y3)**2)
        self.side3 = sqrt((x3 - x1)**2 + (y3 - y1)**2)

    # методы
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def square(self):
        return (sqrt(self.perimeter() * (self.perimeter() - self.side1) * (self.perimeter() - self.side2) *
                (self.perimeter() - self.side3)))

    def height(self, top):  # из какой вершины опущена высота
        if top == 1 or top > 3 or top < 1:
            base = self.side2
        elif top == 2:
            base = self.side3
        elif top == 3:
            base = self.side1
        return self.square() * 2 / base

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class Trapeze:
    # конструктор
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.top1 = [x1, y1]
        self.top2 = [x2, y2]
        self.top3 = [x3, y3]
        self.top4 = [x4, y4]
        self.topx = [x1, x2, x3, x4]
        self.topy = [y1, y2, y3, y4]
        # self.centerx = sum(self.topx) / 4
        # self.centery = sum(self.topy) / 4

    # методы
    def sides(self, topx, topy):
        self.side1 = sqrt((topx[0] - topx[1]) ** 2 + (topy[0] - topy[1]) ** 2)
        self.side2 = sqrt((topx[1] - topx[2]) ** 2 + (topy[1] - topy[2]) ** 2)
        self.side3 = sqrt((topx[2] - topx[3]) ** 2 + (topy[2] - topy[3]) ** 2)
        self.side4 = sqrt((topx[3] - topx[0]) ** 2 + (topy[3] - topy[0]) ** 2)

    # def istrapeze(self):
    #     for i in self.topx:
    #         if abs((self.topx[i] - self.topx[i + 1]) / (self.topy[i] - self.topy[i + 1])):
    #             return True

    def iseqsides(self,):
        if self.side1 == self.side3 or self.side2 == self.side4:
            return True

    def perimeter(self):
        return self.side1 + self.side2 + self.side3 + self.side4

    def square(self):
        if self.iseqsides():
            if self.side1 == self.side3:
                base = abs(self.side2 - self.side4) / 2
                height = sqrt(base**2 + self.side1**2)
                return (self.side2 + self.side4) * height / 2
            elif self.side2 == self.side4:
                base = abs(self.side1 - self.side3) / 2
                height = sqrt(base ** 2 + self.side2 ** 2)
                return (self.side1 + self.side3) * height / 2
        else:
            return False


