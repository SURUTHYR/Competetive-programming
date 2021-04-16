"""
@Author : 
Time complexity :
Space complexity : 
Question link :
"""
class Node:
    def __init__(self,value):
        self.value = value
        self.head = None
class LinkedList:

    def __init__(self):
        self.head = None

    def insert_first(self,value):
        if self.head is None:
            self.head=Node(value)
        curr = self.head
        curr.next = self.head
        self.head = curr
    def insert_last(self,value):
        if self.head is None:
            self.head = Node(value)
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = Node(value)
    def insert_mid(self,value,pos):
        if self.head is None:
            self.head = Node(value)
        count = 1



    #def delete_last(self):
        if self.head is None:
            return -1
        else:
            curr = self.head
            while curr.next.next is not None:
                curr = curr.next
            curr.next = None

    #def delete_mid(self, pos):
        if self.head is None:
            return False
        else:
            val = 0
            curr = self.head
            while val < pos:
                curr = curr.next
                val += 1
            curr.next = curr.next.next

    #def delete_first(self):
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











