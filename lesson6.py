# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

class Triangle:
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    def segmlen(self, pointA, pointB):
        diffx = pointA[0] - pointB[0]
        diffy = pointA[1] - pointB[1]
        invx = diffx ** 2
        invy = diffy ** 2
        return math.sqrt(invx + invy)

    def perimeter(self):
        p12 = self.segmlen(self.point1, self.point2)
        p13 = self.segmlen(self.point1, self.point3)
        p23 = self.segmlen(self.point2, self.point3)
        return p12 + p13 + p23

    def square(self):
        hper = (self.perimeter()/2)
        return math.sqrt(hper * (hper - self.segmlen(self.point1, self.point2))*
                    (hper - self.segmlen(self.point1, self.point3))*
                    (hper - self.segmlen(self.point2, self.point3)))

    def height(self):
        return self.square() / (self.segmlen(self.point1, self.point2) / 2)

triangle1 = Triangle([1, 1], [3,3], [1,6])
print(triangle1.perimeter())
print(triangle1.square())
print(triangle1.height())
