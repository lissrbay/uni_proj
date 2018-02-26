# -*- coding: utf-8 -*-
class Stack:
    def __init__(self):
        self.s = list()
    def push(self, n):
        self.s.append(n)
    def pop(self):
        if len(self.s) > 0:
            self.s.pop()
    def top(self):
        if len(self.s) > 0:
            return self.s[len(self.s) - 1]
    def empty(self):
        return len(self.s) == 0
    
class CheckValidation():
    def check(self, s):
        st = Stack()
        for i in range(0, len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                st.push(s[i])
            else:
                if  not st.empty():
                    c = st.top()
                    if (c == "(" and s[i] == ")") or (c == "[" and s[i] == "]") or (c == "{" and s[i] == "}"):
                        st.pop()
                    else:
                        return False
                else:
                    return False
        return st.empty() 

print("Введите скобочную последовательность для проверки на правильность: ")
s=str(input())  
print("Последовательность правильна?")
c=CheckValidation()
print(c.check(s))