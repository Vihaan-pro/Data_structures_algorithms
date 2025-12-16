# + use func push
# - from the top of the stack 
# to get the item to top use func top
# to check if the stack is empty func is_empty()
# how many items are there use func size

class Stack:
    def __init__(self,n):
        self.stack = []
        self.n = n # max no. of eleements in stacks 
    def push(self,k):
        if len(self.stack)<self.n:
         self.stack.append(k)
        else:
           print("The stack is full")
    def display(self):
        print(self.stack)
    
    def pop(self):
       if len(self.stack)==0:
        print("stack is empty")
       else:
        self.stack.pop(-1)
    def top(self):
       if len(self.stack)==0:
        print("stack is empty")
       else:
          return self.stack[-1]
    def size(self):
       return len(self.stack)
s = Stack(3)
s.display()
s.push(1)
s.display()
s.push(7)
s.display()
s.push(6)
s.display()

print(s.size())

s.pop()
s.display()
print(s.top())
s.display()



