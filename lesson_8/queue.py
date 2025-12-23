class Queue():
    def __init__(self,size):
        self.size = size
        self.queue = [None]*size  # it will create 50 empty slots
        self.front = 0 
        self.rear = 0 
        self.avalaible = size 
    def enqueue (self,item):
        self.queue[self.rear]= item
        self.rear +=1
        self.avalaible -=1
    def print_queue(self):
        print(self.queue)

my_queue = Queue(3)
my_queue.enqueue("ben")
my_queue.enqueue("haily")
my_queue.enqueue("mike")
my_queue.print_queue()