import dlb
class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

l = dlb.PositionalList()
print("Input list plz:")
k = input().split()
for i in k:
	l.add_last(int(i))
v = int(input())
    
def find_sum_of_pair(v):
    i = l._header._next
    j = l._trailer._prev
    last_element = l.last()
    while j != i:
        if i._element + j._element == v:
            return Pair(i._element, j._element)
        if i._element + j._element > v:
            j = j._prev
        if i._element + j._element < v:
            i = i._next
    return None

t = find_sum_of_pair(v)
if t == None:
    print(t)
else:
    print(t.first, t.second)