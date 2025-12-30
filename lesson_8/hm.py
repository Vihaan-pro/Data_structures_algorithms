class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(f"{item} pushed into stack")

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        return self.items.pop()

    def top(self):
        if self.is_empty():
            print("Stack is empty. No top element.")
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# -------- Main Program --------
s = Stack()

s.push(10)
s.push(20)
s.push(30)

print("Top element:", s.top())

print("Popped element:", s.pop())

print("Stack size:", s.size())

print("Is stack empty?", s.is_empty())

print("Popped element:", s.pop())
print("Popped element:", s.pop())

s.pop()
