# -*- coding: utf-8 -*-
print("Введите последовательность: ")
A=list(input().split())
print("Введите сдвиг: ")
k=int(input())
if(len(A)>0):
	for i in range(k%len(A)):
		temp=A[len(A)-1]
		for j in range(len(A)-1,0,-1):
			A[j] = A[j-1]
		A[0]=temp
 
for i in A:
	print(i,end=" ")