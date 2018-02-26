import dlb
		
class DoublyLinkedCircularList(dlb.DoublyLinkedBase):
    def __init__ (self):
        self._header = dlb._Node(None, None, None)
        self._header._next = self._header
        self._header._prev = self._header
        self._size = 0
    def insert_first(self, e):
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        self._insert_between(e, self._header._prev, self._header)
        
    def delete_first(self):
        if self.is_empty( ):
            raise dlb.Empty("List is empty")
        return self._delete_node(self._header._next)

    def delete_last(self):
        if self.is_empty( ):
            raise dlb.Empty("List is empty")
        return self._delete_node(self._header._prev)    
    
    def __str__(self):
        s = '['
        if self._size != 0:
            x = self._header._next         
            s += str(x._element)
            while x._next._element != None:
                x = x._next
                s += ', ' + str(x._element)
        return s + ']'
    
c = DoublyLinkedCircularList()
print("Example:")
c.insert_first(1)
c.insert_first(2)
c.insert_last(3)
c.delete_last()
c.insert_last('meow')

x = c._header._next 
print("Cycle three times: ")
count = 0        
while count < 3:
	if x._element != None:
		print(x._element)
	x = x._next
	if x._element == None:
		count += 1
        
print("List: ", c)
