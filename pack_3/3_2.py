# -*- coding: utf-8 -*-
a = ( 1,   4,    5,   9,    10,  40,  50,   90,  100, 400,  500, 900,  1000)
r = ('I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M')
class RomanNumber(int):
	def arab_to_roman(self, n):
		if n == 0:
			res= 'У римлян нет нуля'
			return res
		res = ''
		for i in range(13):
			res += n // a[12 - i] * r[12 - i]
			n %= a[12-i]
		return res
		
	def roman_to_arab(self, roman):
		m = 12
		len_s = len(roman)
		arab = 0
		n = m
		i = 0
		while(n >= 0 and i < len_s):
			if roman[i] == r[n] and ( not n % 2 or roman[i + 1] == r[n]):
				arab += a[n]
				i += 1 + n % 2
			else:
				n -= 1
		return arab

c=RomanNumber()
print("Введите число для перевода в римскую систему счисления: ")
n=int(input())
print("Результат: ",c.arab_to_roman(n))
print("Введите число для перевода в арабскую систему счисления: ")
s=str(input())
print("Результат: ",c.roman_to_arab(s))
