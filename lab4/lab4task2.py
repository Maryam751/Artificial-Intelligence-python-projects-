class Queue:

    def __init__(self):
        self.queue = []

    # add element 
    def enqueue(self, value):
        self.queue.append(value)
        print(value, "added to queue")

    # remove element 
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            value = self.queue.pop(0)
            print(value, "removed from queue")

    # display front element
    def front(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Front element:", self.queue[0])

    # display  elements
    def display(self):
        print("Queue:", self.queue)


# create Queue object
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.display()
q.front()
q.dequeue()
q.dequeue()
q.display()
q.front()