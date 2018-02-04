class Node:
    def __init__(self, key, data, left_p = None, right_p = None, parent_p = None):
        self.key = key
        self.data = data
        self.left_child = left_p
        self.right_child = right_p
        self.parent = parent_p
        
    def isLeftChild(self):
        return self.parent and self.parent.left_child == self
    
    def isRightChild(self):
        return self.parent and self.parent.right_child == self
    
    def exLeftChild(self):
        return self.left_child
    
    def exRightChild(self):
        return self.right_child
    
    def exLeftOrRightChild(self):
        return self.right_child or self.left_child
    
    def exLeftAndRightChild(self):
        return self.right_child and self.left_child
    
    def isRoot(self):
        return not self.parent
    
    def isLeaf(self):
        return not(self.left_child or self.right_child)
    
    def replaceData(self, key, data, left_p, right_p):
        self.key = key
        self.data = data
        self.left_child = left_p
        self.right_child = right_p
        if self.exLeftChild():
            self.leftChild.parent = self
        if self.exRightChild():
            self.rightChild.parent = self
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
        
    def __len__(self):
        return self.size
    
    def put(self, key, data):
        if self.root:
            self._put(key, data, self.root)
        else:
            self.root = Node(key, data)
        self.size += 1
    
    def _put(self, key, data, currentNode):
        if currentNode.key < key:
            if currentNode.exRightChild():
                self._put(key, data, currentNode.right_child)
            else:
                currentNode.right_child = Node(key, data, parent_p = currentNode)
        else:
            if currentNode.exLeftChild():
                self._put(key, data, currentNode.left_child)
            else:
                currentNode.left_child = Node(key, data, parent_p = currentNode)
                
    def __setitem__(self, key, data):
        self.put(key, data)
    
    def get(self, key):
        if self.root:
            result = self._get(key, self.root)
            if result:
                return result.data
            else:
                return None
        else:
            return None
        
    def _get(self, key, currentNode):
        if currentNode == None:
            return None
        elif currentNode.key == key:
            return currentNode
        elif currentNode.key > key:
            return self._get(key, currentNode.left_child)
        else:
            return self._get(key, currentNode.right_child)
        
    def __getitem__(self, key):
        return self.get(key)
    
    def delete(self, key):
        if self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        elif self.size > 1:
            deletingNode = self._get(key, self.root) 
            if deletingNode:
                self._delete(deletingNode)
                self.size -= 1
            else:
                return "Key not Found"
        else:
            return "Key not Found"
    
    def _delete(self, currentNode):
        if currentNode.isLeaf():
            if currentNode.parent.left_child == currentNode:
                currentNode.parent.left_child = None
            else:
                currentNode.parent.right_child = None
        else:
            if currentNode.exLeftAndRightChild():
                return "Error" #что тут делать мм?
            elif currentNode.exLeftChild():
                if currentNode.isLeftChild():
                    currentNode.parent.left_child = currentNode.left_child
                    currentNode.left_child.parent = currentNode.parent
                elif currentNode.isRightChild():
                    currentNode.parent.right_child = currentNode.left_child
                    currentNode.left_child.parent = currentNode.parent
                else:
                    currentNode.replaceData(currentNode.left_child.key, currentNode.left_child.data,
                                           currentNode.left_child.left_child, currentNode.left_child.right_child)
            else:
                if currentNode.isRightChild():
                    currentNode.parent.right_child = currentNode.right_child
                    currentNode.right_child.parent = currentNode.parent
                elif currentNode.isLeftChild():
                    currentNode.parent.left_child = currentNode.right_child
                    currentNode.right_child.parent = currentNode.parent
                else:
                    currentNode.replaceData(currentNode.right_child.key, currentNode.right_child.data,
                                           currentNode.right_child.left_child, currentNode.right_child.right_child)
    
def __iter__(self):
    if self:
        if self.exLeftChild():
            for data in self.left_chiLd:
                yield data
    yield self.key
    if self.exRightChild():
        for data in self.right_child:
            yield data 
                
#tree = BinarySearchTree()
#tree[1]="АТЧ"
#tree[2]="Матан"
#tree[3]="Геома"
#tree[4]="Инфа"

#print(tree[6])
#print(tree[2])    
#tree.delete(2)
#print(tree[3])
#print(tree[2])