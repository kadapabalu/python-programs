class CircularQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.front = 0
        self.rear = 0
        self.size = size
    def enqueue(self, item):
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.size

    def display(self):
        print(self.queue)
cq = CircularQueue(5)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.display()
