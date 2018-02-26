f = open("fenwick.in", "r")
f2 = open("fenwick.out", "w")
def add(x, val):
	while x < n + 1:
		t[x] += val
		x = x | (x + 1) 
def sum_up(x):
	res = 0
	while x > 0:
		res += t[x]
		x = (x & (x + 1)) - 1
	return res
def sum(l, r):
	return sum_up(r) - sum_up(l - 1)

n = int(f.readline()) #длина массива
k = int(f.readline()) #количество запросов
t = [ 0 for i in range(n + 1)]

for i in range(k):
	a = list(f.readline().split())
	if str(a[0]) == 'ADD':
		add(int(a[1]), int(a[2])) #добавление элемента
	else:
		u = sum(int(a[1]), int(a[2])) #сумма на l, r 
		f2.write(str(u))
		f2.write("\n")
f.close()
f2.close()