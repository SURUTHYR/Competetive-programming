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

    def insert_last(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
