print("Input the polynomial(ex. 5x^2+4x^3-7-13x, the order doesn't matter): ")
a = str(input()) 

def num():
	global j
	c = ''
	while j < len(a) and not (a[j] == "x" or a[j] == "-" or a[j] == "+"):
			c += a[j]
			j += 1
	if not c == '': 
		return int(c)
	else:
		return 1
	
j = 0; b = 0
p, st, sign = [], [], []

if a[0] == '-':
	sign.append("-")
	j += 1
else:
	sign.append("+")

while j < len(a):
	c = num()
	if j < len(a) and a[j] == 'x':
		if j + 1 < len(a) and a[j + 1] == '^':
			j += 2
			d = num()
			st.append(d - 1)
			p.append(c * d)
		else:
			st.append(0)
			p.append(c)
	else:
		st.append(-1)
		p.append(-1)
	b = j + 1
	if  j < len(a) and (a[j] == "-" or a[j] == "+"):
		sign.append(a[j])
	j += 1
	
print("The first derivative: ")	
for i in range(len(p)):
	if not((i == 0) and sign[i] == "+"):  
		if not(p[i] == -1 and st[i] == -1):
			print(sign[i], end = "")
	if p[i] > 0:
		print(p[i], end  = "")
	if  st[i] > 0:
		if st[i] == 1:
			print("x", end = "")
		else:
			print("x^", end = "")
			print(st[i], end = "")

