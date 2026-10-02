class Stack:

    def __init__(self):
        self.stack = []   #create stack

    # add element to stack
    def push(self, value):
        self.stack.append(value)
        print(value, "pushed into stack")

    # remove element from stack
    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            value = self.stack.pop()
            print(value, "popped from stack")

    # display top element
    def Top(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Top element:", self.stack[-1])

    # display all elements
    def display(self):
        print("Stack:", self.stack)
       # print(self.stack[::-1]) # reverse order of stack

# create stack 
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.display()
s.Top()
s.pop()
s.display()
s.Top()