# -*- coding: utf-8 -*-
from math import floor
from math import sqrt
print("Введите число: ")
a=int(input())
sum=0
if(a>1):
	for i in range(1,floor(sqrt(a))+1, 1):
		if a%i==0:
			sum=sum+a//i+i

if sum/2==a:
		print("Purrfect")
else:
	print("Not perfect")
