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


class LinkedList:
    def __init__(self):
        self.head = None

    # createNode and and make linked list
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    def print(self):
        temp = self.head
        while(temp):
            print(temp.value,end="->")
            temp=temp.next
        print()

    # Function to get the nth node from
    # the last of a linked list
    def printNthFromLast(self, n):
        temp = self.head  # used temp variable

        length = 0
        while temp is not None:
            temp = temp.next
            length += 1

        # print count
        if n > length:  # if entered location is greater
            # than length of linked list
            print('Location is greater than the' +
                  ' length of LinkedList')
            return
        temp = self.head
        for i in range(1, length - n):
            temp = temp.next
        print(temp.value)


# Driver Code
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(35)
llist.print()
llist.printNthFromLast(4)

