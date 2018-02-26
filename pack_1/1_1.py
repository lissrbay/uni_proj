# -*- coding: utf-8 -*-
def arithmetic(first, second, operation):
	if(operation == "+"):
		return print(first + second)
	elif operation == "-":
		return print(first - second)
	elif operation == "*":
		return print(first * second)
	elif operation == "/":
		if second == 0:
			return print("На ноль делить нельзя.")
		else:
			return print(first/second)
	else: 
		return print("Unknown operation")
		
print("Введите два числа и арифметическую операцию: ")
a,b,c=input().split();
print("Результат: ")
arithmetic(int(a),int(b),str(c))

