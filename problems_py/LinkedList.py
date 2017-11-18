class Node():
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class LinkedList():
    def __init__(self):
        self.first = None
        self.size = 0
        self.last = None
        
    def __str__(self):
        if self.first != None:
            x = self.first
            s = ''
            s += '[' + str(x.value)
            while x.next != None:
                x = x.next
                s += ', ' + str(x.value)
        return s + ']'
    
    def add(self, value = None, pos = -1): #по умолчанию добавляет элемент в конец списка
        self.size += 1
        if self.first == None:
            self.first = self.last = Node(value, None)
            return
        if pos == 0:
            self.first = Node(value, self.first)
            return
        if pos == -1:
            self.last.next = Node(value, None)
            self.last = self.last.next
            return
        x = self.first
        count = 0
        while x != None:
            count += 1
            if count == pos:
                x.next = Node(value, x.next)
                if x.next.next == None:
                    self.last = x.next
                break
            x = x.next
        
    def delete(self, pos = -1): #по умолчанию удаляет последний элемент списка 
        if (self.first == None):
            return
        x = self.first
        count = 0
        if pos == -1:
            pos = self.size - 1
        self.size -= 1
        if pos == 0:
            self.first = self.first.next
            return
        
        while x != None:
            if count == pos:
                if x.next == None:
                    self.last = old
                old.next = x.next 
                break
            old = x  
            x = x.next
            count += 1
            
    def find(self, value = None): #возвращает первое вхождение элемента в список
        if value == None or self.first == None:
            return None
        count = 0
        x = self.first
        while x != None:
            if x.value == value:
                return count
            x = x.next
        return None
            
c = LinkedList()
c.add(1)
c.add(2, 0)
c.add(45)

c.delete()
c.delete(0)
c.add(5)
print(c.find(4))
print(c.find(5))
print(c.size)
print(c)