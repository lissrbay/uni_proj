class _Node:
    def __init__(self, _element, _sitename, _prev,_next):
        self._element =_element
        self._sitename = _sitename
        self._prev =_prev
        self._next =_next

class DoublyLinkedBase:
    def __init__ (self):
        self._header = _Node(0, None, None, None)
        self._trailer = _Node(100000, None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, url, predecessor, successor):

        newest = _Node(e, url, predecessor, successor) 
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest
    
    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        node._prev = node._next = node._element = None
       
    def _find(self, name):
        x = self._header
        while(x != self._trailer):
            if x._sitename == name:
                return x
            x = x._next
        return False
            
class DoublyLinkedList(DoublyLinkedBase):
    def from_site(self, url):
        s = self._find(url)
        if s == False:
            return self._insert_between(1, url, self._header, self._header._next)       
        x = s
        count = s._element
        while(x != self._trailer):
            if count + 1 <= x._next._element:
                self._insert_between(count + 1, url, x, x._next)
                return self._delete_node(s)
            x = x._next
        return self._insert_between(count + 1, url, self._trailer._prev, self._trailer)
    
    def from_client(self, count):
        if not self.is_empty():
            x = self._trailer._prev  
            i = 1
            print("Top", count, "sites: ")
            while x != self._header and i <= count:
                print(str(i) + ')', x._sitename)
                i += 1
                x = x._prev
            print()
			
b = DoublyLinkedList()
base = DoublyLinkedList()

def menu():
	print("Type 'E' for exit.")
	print("Type 'u' to call \"from_site\".")
	print("Type 'g' to call \"from_client\"")
	print("Example:")
	print("from_site(\"lookatme.ru\")\nfrom_site(\"yandex.ru\") \nfrom_site(\"google.com\") \nfrom_site(\"yandex.ru\")")
	b.from_site("lookatme.ru")
	b.from_site("yandex.ru")
	b.from_site("google.com")
	b.from_site("yandex.ru")
	print("from_client(2)")
	b.from_client(2)
	print("from_site(\"lookatme.ru\")\nfrom_site(\"github.com\") \nfrom_site(\"github.com\") \nfrom_site(\"lookatme.ru\")")
	b.from_site("lookatme.ru")
	b.from_site("lookatme.ru")
	b.from_site("github.com")
	b.from_site("github.com")
	print("from_client(3)")
	b.from_client(3)
	while True:
		n = str(input())
		if n == 'E':
			return 0
		if n == 'u':
			print("Input url: (Type 's' to stop adding sites.)")
			k = ''
			while True:
				k = str(input())
				if k == 's':
					break
				base.from_site(k)
			continue
		if n == 'g':
			print("Input count of sites:")
			k = int(input())
			base.from_client(k)
			continue
		print("Unknown operation.")

menu()
