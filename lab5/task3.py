class PriorityQueue:
    def __init__(self):
        self.pq = []

    def push(self, priority, item):
        self.pq.append((priority, item))

    def pop(self):
        self.pq.sort()
        return self.pq.pop(0)

    def display(self):
        while self.pq:
            priority, item = self.pop()
            print(item, "Priority:", priority)

pq = PriorityQueue()
pq.push(3, "C")
pq.push(1, "A")
pq.push(2, "B")
pq.push(4, "D")
pq.push(6, "F")
pq.push(5, "E")

pq.display()




