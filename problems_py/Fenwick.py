f = open("fenwick.in", "r")
f2 = open("fenwick.out", "w")
def add(x, y, val):
	i = x
	j = y
	while(i < n + 1):
		while(j < m + 1):
			t[i][j] += val
			j = j | (j + 1)
		i = i | (i + 1)
		j = y
def sum_up(x, y):
	res = 0
	i = x
	j = y
	while(i > 0):
		while(j > 0):
			res += t[i][j]
			j = (j & (j + 1)) - 1
		i = (i & (i + 1)) - 1
		j = y
	return res
def sum(x1, y1, x2, y2):
	return sum_up(x2, y2) + sum_up(x1 - 1, y1 - 1) - sum_up(x1 - 1, y2) - sum_up(x2, y1 - 1)

n = int(f.readline()) 			#длина массива
m = n 							#ширина массива
k = int(f.readline())   #количество запросов
t = [ (m + 1) * [0] for i in range(n + 1)]

for i in range(k):
	a = list(f.readline().split())
	if str(a[0]) == 'ADD':
		add(int(a[1]), int(a[2]), 1) #добавление элемента
	else:
		u = sum(min(int(a[1]), int(a[3])), min(int(a[2]), int(a[4])), max(int(a[1]), int(a[3])), max(int(a[2]), int(a[4]))) #сумма на l1, r1, l2, r2 
		f2.write(str(u))
		f2.write("\n")
f.close()
f2.close()