# -*- coding: utf-8 -*-
from math import floor
from math import sqrt
print("Введите число для проверки на простоту: ")
a=int(input())

p = False
for i in range(2,floor(sqrt(a))+1, 1):
    if a%i==0:
        p = True
if p:
    print("Составное") 
else:
    print("Простое") 

