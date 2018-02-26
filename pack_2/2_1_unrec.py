# -*- coding: utf-8 -*-
def factorial(n):
    res=1
    for i in range(2,n+1):
        res *= i;
    return res
print("Введите число: ")
n=int(input())
print("Результат: ")
print(factorial(n))
