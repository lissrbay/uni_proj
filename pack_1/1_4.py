# -*- coding: utf-8 -*-
print("Введите строку для проверки на палиндромность: ")
s = str(input())

palindrome = (s[: len(s) / 2] == s[len(s) : len(s) / 2 - 1 + len(s) % 2 : -1])
if palindrome:
	print("Да.")
else:
	print("Нет.")
