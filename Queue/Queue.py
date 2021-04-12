class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        if(self.queue == []):
            return True
        return False

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if(self.is_empty()):
            print("The queue is empty")
            return -1
        else:
            return(self.queue.pop(0))

    def peek(self):
        if (self.is_empty()):
            print("The queue is empty")
            return -1
        else:
            return (self.queue[-1])

