# -*- coding: utf-8 -*-
from math import pi

class Circle():
    def __init__(self, rad):
        self.radius = rad
    def area(self): 
        return pi * (self.radius ** 2)
    def perimeter(self):
        return 2 * pi * self.radius
    
class Rectangle():
	def __init__(self, a, b):
		self.width = a
		self.length = b
	def area(self):
		return self.width * self.length
	def perimeter(self):
		return self.width * 2 + self.length * 2
		
print("Радиус окружности: ")		
n = int(input())
c = Circle(n)
print("Ширина и длина прямоугольника: ")
a, b = input().split()
p = Rectangle(int(a), int(b)) 

print("Площадь круга: ", c.area())
print("Периметр круга: ", c.perimeter())
print("Площадь прямоугольника: ", p.area())
print("Периметр прямоугольника: ", p.perimeter())
