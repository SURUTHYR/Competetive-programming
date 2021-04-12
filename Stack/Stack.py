class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if(self.stack == []):
            return True
        return False

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if(self.is_empty()):
            print("The stack is empty")
            return -1
        else:
            return(self.stack.pop())

    def peek(self):
        if (self.is_empty()):
            print("The stack is empty")
            return -1
        else:
            return (self.stack[-1])

