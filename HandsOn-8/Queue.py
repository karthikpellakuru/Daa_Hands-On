class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [-1] * size
        self.front = 0
        self.rear = 0

    def enqueue(self, item):
        if self.rear == self.size:
            print("Queue is full")
        else:
            self.queue[self.rear] = item
            self.rear += 1

    def dequeue(self):
        if self.front == self.rear:
            print("Queue is empty")
        else:
            item = self.queue[self.front]
            self.front += 1
            return item

# Example 
size = int(input("Enter the size of the queue: "))
queue = Queue(size)
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())
