class Stack:
    def __init__(self, limit):
        self.items = []
        self.limit = limit

    def push(self, value):
        if self.size() == self.limit:
            print("Cannot push, stack overflow")
        else:
            self.items.append(value)
            print(value, "pushed into stack")

    def pop(self):
        if self.is_empty():
            print("Cannot pop, stack underflow")
        else:
            removed = self.items.pop()
            print(removed, "removed from stack")

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Top element is:", self.items[-1])

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def show(self):
        print("Current Stack:", self.items)


# Testing the stack
s = Stack(4)

s.show()
s.push("Apple")
s.push("Banana")
s.push("Cherry")
s.show()

s.peek()
print("Stack size:", s.size())

s.pop()
s.show()

s.push("Date")
s.push("Elderberry")  # overflow example
s.show()
