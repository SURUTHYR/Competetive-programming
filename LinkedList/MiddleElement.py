"""
@Author : 
Time complexity :
Space complexity : 
Question link :
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None
        self.root = None

    def print(self):
        temp = self.root
        while (temp):
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new = Node(value)
        if (self.head == None):
            self.head = new
            self.root = new
        else:
            self.head.next = new
            self.head = new

    def middle(self):
        i1 = i2 = self.root
        if (i1 is not None):
            while (i1 is not None and i1.next is not None):
                i1 = i1.next.next
                i2 = i2.next
            print("Middle is: ", i2.value)


if __name__ == "__main__":
    llist = Linked_List()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(5)
    llist.push(6)
    llist.push(7)
    llist.push(8)
    llist.push(9)
    llist.push(10)
    llist.middle()