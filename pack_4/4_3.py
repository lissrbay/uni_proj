import random 					#правила симуляции:
x = 0		  					#сначала все звери ходят
n = 0         					#затем вычисляется кто кого съел и кто где сдох
iter = 0      					#потом на свободные места заселяются дети(если есть)
random.seed() 					#дети могут рождаться и заполнять место быстрее, чем умирают их предки
river = []    					#(в инструкции не сказано ничего по этому поводу) 
child = []    					#хотя логически (и биологически) это не особо верно вроде как
uses = [0 for i in range(101)]  #река двухмерная, тк в каждой точке может находится две особи

class Fish():
	def __init__(self):
		self.char = 'F'
		self.type = 1
		self.step = 0
		
class Bear():
	def __init__(self, x):
		self.char = 'B'
		self.hungry = x 
		self.type = 2
		self.step = 0

class Cell():
	def __init__(self, k):
		self.arr = []
		if k == 0:
			pass
		if k == 1:
			self.arr.append(Fish())	
		if k == 2:
			self.arr.append(Bear(x))
	def size(self):
		return len(self.arr)
	def pop(self, st):
		if len(self.arr) > 0:
			self.arr[len(self.arr) - 1].step = st 
			c = self.arr[len(self.arr) - 1]
			self.arr.pop()
			return c
		return Fish()
	def add(self, k):
			self.arr.append(k)
	def collide(self):
		if (self.arr[0].char == 'F' and self.arr[1].char == 'B'):
			self.arr[1].hungry = x
			self.arr.pop(0)
			return 0
		elif (self.arr[1].char == 'F' and self.arr[0].char == 'B'):
			self.arr[0].hungry = x	
			self.arr.pop()
			return 0 
		elif (self.arr[1].char == 'F' and self.arr[0].char == 'F'):
			return 1
		elif (self.arr[1].char == 'B' and self.arr[0].char == 'B'):
			self.arr[0].hungry -=  1
			self.arr[1].hungry -=  1
			if self.arr[1].hungry <= 0:
				self.arr.pop()
			if self.arr[0].hungry <= 0:
				self.arr.pop(0)
			return 2
	def feed(self):
		self.arr[0].hungry -= 1
		if self.arr[0].hungry <= 0:
				self.arr.pop()
	def char(self, pos):
		if pos + 1 <= len(self.arr):
			return (self.arr[pos].char)
		else:
			return '~'
	def use(self, ind):
		return self.arr[ind].step
	def replace(self, p, j):
			self.arr[j] = p
			self.arr[j].hungry = x
		
for i in range(101):
		river.append(Cell(0))
		
def new_game():
	global n
	global x
	global iter
	print("Type size of a river (<=100): ")
	n = int(input())
	print("Type amount of bear's hungry: ")
	x = int(input())
	print("Type number of iterations: ")
	iter = int(input())
	print("Type number of Fish(Fish + Bears < n !): ")
	f = int(input())
	print("Type number of Bears(Fish + Bears < n !): ")
	b = int(input())
	for i in range(n):
		river[i] = (Cell(0))
	for i in range(n):
		uses[i] = 0
	put_animal(f, 1)
	put_animal(b, 2)
	
	
def check_fish(i, k, pos, pos2):
	if  river[i].size == 2 and river[i].type(pos) == 2:
		if river[i + k].type(pos2) == 1:
			t = river[i].pop(st)
			river[i + k].replace(t, pos2)
	return 0
	
def put_animal(num, animal):
	while num > 0:
		k = random.randint(0, n - 1)
		if uses[k] == 0:
			river[k] = Cell(animal)
			uses[k] = 1
			num  -= 1
			
def output():
	for j in range(2):
		for i in range(n):
				print(river[i].char(j), end = "")
		print()
	print()
		
def put_child():
	for i in range(n):
			if river[i].size() == 0 and len(child) > 0:
				river[i] = Cell(child[0])
				child.pop(0)
	child.clear()	
	
def make_step(st):
	for i in range(n):
			for j in range(river[i].size()-1, -1, -1):
				if river[i].use(j) < st:
					k = random.randint(0, 1)
					if k == 0:
						k = -1
					if i + k < n and i + k >= 0  and river[i + k].size() < 2:
						t = river[i].pop(st)
						river[i + k].add(t)
					elif i + k < n and i + k >= 0 and river[i + k].size() == 2:
						u = check_fish(i, k, 0, 0) + check_fish(i, k, 0, 1) + check_fish(i, k, 1, 0) + check_fish(i, k, 1, 1)
	
def collision():
	for i in range(n):
			if river[i].size() == 2:
				p = river[i].collide()
				if p == 1 or p == 2:
					child.append(p)
				continue
			if river[i].size() == 1 and river[i].arr[0].type == 2:
				river[i].feed()
				
def game():
	for i in range(iter):
		output()
		make_step(i + 1)
		collision()
		put_child()
	
def menu():
	while True:
		print("Type: \n - \"N\" for a new simulation \n - \"E\" for exit")
		s = str(input())
		if s == 'N':
			new_game()
			game()
		elif s == 'E':
			return 0
		else: 
			print("Type another command. ")
			
menu()		