class Queue:
    def __init__(self):
        self.queue = []

    def insert(self, element):
        self.queue.append(element)

    def remove(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            print("The queue is empty")

# create a new queue
queue = Queue()

# insert elements into queue
queue.insert(5)
queue.insert(6)
print(queue.remove())

queue.insert(7)
print(queue.remove()) 
print(queue.remove())
print(queue.remove()) 