class Queue_using_stacks:
    def __init__(self):
        self.inputstack = [] # enqueue
        self.outputstack = [] # dequeue
    def enqueue(self,item):
        self.inputstack.append(item)
        print("the item added is",item)
    def print_queue(self):
        queuestate = self.outputstack[::-1]+ self.inputstack
        print(queuestate)
    def dequeue (self):
        self.outputstack

myqueuestack = Queue_using_stacks()
myqueuestack.enqueue("roger")
myqueuestack.enqueue("Rafel")
myqueuestack.enqueue("Adam")
myqueuestack.enqueue("karol")
myqueuestack.enqueue("Chris")
myqueuestack.enqueue("alaxander")
myqueuestack.print_queue()