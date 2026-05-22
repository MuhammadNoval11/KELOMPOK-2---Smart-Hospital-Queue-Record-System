# linked_list.py

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        baru = Node(data)
        if self.head is None:
            self.head = baru
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = baru

    def hapus(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        curr = self.head
        while curr.next:
            if curr.next.data == data:
                curr.next = curr.next.next
                return
            curr = curr.next

    def tampil(self):
        if self.head is None:
            print("kosong")
            return
        curr = self.head
        while curr:
            print(curr.data, end=" -> " if curr.next else "\n")
            curr = curr.next