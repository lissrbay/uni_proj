# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(20000)
def factorial_v2(n):
    if n==0:
        return 1
    else:
        return n*factorial_v2(n-1)
print("Введите число: ")
n=int(input())
print("Результат: ")
print(factorial_v2(n))

