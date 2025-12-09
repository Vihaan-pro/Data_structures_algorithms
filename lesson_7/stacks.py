# + use func push
# - from the top of the stack 
# to get the item to top use func top
# to check if the stack is empty func is_empty()
# how many items are there use func size

class Stack:
    def __init__(self,n):
        self.stack = []
        self.n = n
    def push(self,k):
        self.stack.append(k)
    def display(self):
        print(self.stack)

s = Stack(3)
s.display()
s.push(1)
s.display()
s.push(7)
s.display()
s.push(6)
s.display()
s.push(10)
s.display()


