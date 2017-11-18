# -*- coding: utf-8 -*-
from math import floor
from math import sqrt
print("Введите число: ")
a=int(input())
b=[]
for i in range(1,floor(sqrt(a))+1, 1):
	if a%i==0:
		b.append(a//i)
		b.append(i)

b.sort()
for i in b:
	print(i, end=" ")

