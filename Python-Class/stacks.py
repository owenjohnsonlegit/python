class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            print("The stack is empty")

# create a new stack
stack = Stack()

# push elements onto stack
stack.push(5)
stack.push(6)
print(stack.pop()) 

stack.push(7)
print(stack.pop()) 
print(stack.pop()) 
print(stack.pop()) 