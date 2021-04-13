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

    # O(n)
    def insert_last(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(value)

    # O(1)
    def insert_first(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            temp = self.head
            self.head = Node(value)
            self.head.next = temp

    # O(n)
    def insert_mid(self, value, pos):
        if self.head is None:
            self.head = Node(value)
        else:
            val = 0
            curr = self.head
            while  curr.next is not None and val < pos:
                curr = curr.next
                val += 1
            temp = curr.next
            curr.next = Node(value)
            curr.next.next = temp


    def delete_last(self):
        if self.head is None:
            return -1
        else:
            curr = self.head
            while curr.next.next is not None:
                curr = curr.next
            curr.next = None

    def delete_mid(self, pos):
        if self.head is None:
            return False
        else:
            val = 0
            curr = self.head
            while val < pos:
                curr = curr.next
                val += 1
            curr.next = curr.next.next

    def delete_first(self):
        if self.head is None:
            return False
        self.head = self.head.next

    def print(self):
        temp = self.head
        while(temp):
            print(temp.value,end="->")
            temp=temp.next
        print()
obj = LinkedList()
obj.insert_first(1)

obj.insert_last(2)
obj.insert_last(3)
obj.insert_last(4)
obj.insert_mid(9,2)
obj.print()
obj.delete_first()
obj.print()
obj.delete_last()
obj.print()
obj.delete_mid(0)
obj.print()











