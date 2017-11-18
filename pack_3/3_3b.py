# -*- coding: utf-8 -*-
#типа пример с наследованием
from math import pi
		
class Figure():
	def area(self, a, b):
		return a * b
	def perimeter(self, a, b):
		return 2 * (a + b)
		
class Circle(Figure):
    def __init__(self, rad):
        self.radius = rad
    def area(self): 
        return Figure.area(self, self.radius, self.radius * pi)
    def perimeter(self):
        return Figure.perimeter(self, pi * self.radius, 0)
    
class Rectangle(Figure):
	def __init__(self, a, b):
		self.width = a
		self.length = b
	def area(self):
		return Figure.area(self, self.width, self.length)
	def perimeter(self):
		return Figure.perimeter(self, self.width, self.length)

print("Type shape(circle or rectangle): ")		
n = str(input())

if n == 'Circle' or n == 'circle':
	print("Радиус окружности: ")		
	n = int(input())	
	c = Circle(n)
else:
	print("Ширина и длина прямоугольника: ")
	a, b = input().split()
	c = Rectangle(int(a), int(b))
import os
os.system('cls')
print("Площадь: ", c.area(), "Периметр: ", c.perimeter())



