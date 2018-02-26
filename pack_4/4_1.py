def get_time(line):
    return int(line[0:2]) * 60 * 60 * 1000 + int(line[3:5]) * 60 * 1000 + int(line[6:8]) * 1000 + int(line[9:12])
def time(t):
	h = t // 3600000 
	m = (t - h *3600000) // 60000
	s = (t - h *3600000 - m * 60000) //1000
	ms = (t - h *3600000 - m * 60000 - s * 1000)
	return str(h) + ":" + str(m) + ":" + str(s) + ":" + str(ms)
class Cell():
	def __init__(self):
		self.s = list()
	def push(self, n):
		self.s.append(n)
	def pop(self):
		if len(self.s) > 0:
			self.s.pop(0)
	def front(self):
		if len(self.s) > 0:
			return self.s[0]
		else:
			return 0
	def empty(self):
		return len(self.s) == 0
	def size(self):
		return len(self.s)
	
left = 0			
d = {'V': None, 'D': None, 'X': None, 'Y': None, 'B': None, 'J': None, 'Q': None, 'Z': None, 'K': None, 'P': None, 'All': None}
mx = {'V': 0, 'D': 0, 'X': 0, 'Y': 0, 'B': 0, 'J': 0, 'Q': 0, 'Z': 0, 'K': 0, 'P': 0, 'All': 0}
mx_l = {'V': 0, 'D': 0, 'X': 0, 'Y': 0, 'B': 0, 'J': 0, 'Q': 0, 'Z': 0, 'K': 0, 'P': 0, 'All': 0}

f = open("TRD2.csv", "r")
a = f.readline()
for i in d:
	d[i] = Cell()
			
def count(pos, t):
		w =  d[pos].front()
		while t - w > 1000 and not d[pos].empty():
			w =  d[pos].front()
			d[pos].pop()			
		d[pos].push(t)
		if mx[pos] < d[pos].size():		
			mx[pos] = d[pos].size()
			mx_l[pos] = d[pos].front()
def work():
	global left 
	flag = False
	while True:
		a = f.readline()
		s = a.split(',')
		if(s[0] == ''):
			return 0
		if not flag:
			left = get_time(s[0])
			flag = True
		t = get_time(s[0]) - left
		count(s[3][0], t)
		count('All', t)
			
def output():
	for i in d:
		print(i, "Maximum number of trades - ", mx[i], " take place at ", time(mx_l[i] + left))
work()
output()
f.close()		