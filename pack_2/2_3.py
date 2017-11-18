# -*- coding: utf-8 -*-
	
print("Введите число строк треугольника Паскаля: ")
a=int(input())
d=[[0] * a for i in range(2)]
d[0][0]=1
s=" "
print(s*a, end="")
print(d[0][0])
for i in range(1,a):
	print(s*(a-i), end="")
	d[1][0]=1
	print(d[1][0], end=" ")
	for j in range(1,i):
		d[1][j]=d[0][j-1]+d[0][j]
		print(d[1][j], end=" ")
	d[1][i]=1
	for j in range(0,i+1):
		d[0][j]=d[1][j]
	print(d[1][i])
