import time
import random

# stack
class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "stack kosong"

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


# queue
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return "queue kosong"

    def is_empty(self):
        return len(self.items) == 0


# bst
class Node:
    def __init__(self, data):
        self.data = data
        self.kiri = None
        self.kanan = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if node.kiri is None:
                node.kiri = Node(data)
            else:
                self._insert(node.kiri, data)
        else:
            if node.kanan is None:
                node.kanan = Node(data)
            else:
                self._insert(node.kanan, data)

    def search(self, data):
        return self._search(self.root, data)

    def _search(self, node, data):
        if node is None:
            return False
        if node.data == data:
            return True
        elif data < node.data:
            return self._search(node.kiri, data)
        else:
            return self._search(node.kanan, data)


# benchmark
ukuran = [100, 1000, 10000]

for n in ukuran:
    data = [random.randint(1, 10000) for _ in range(n)]
    print(f"n = {n}")

    s = Stack()
    awal = time.time()
    for x in data:
        s.push(x)
    print(f"  stack push  : {(time.time() - awal) * 1000:.4f} ms")

    awal = time.time()
    for _ in range(n):
        s.pop()
    print(f"  stack pop   : {(time.time() - awal) * 1000:.4f} ms")

    q = Queue()
    awal = time.time()
    for x in data:
        q.enqueue(x)
    print(f"  queue enqueue: {(time.time() - awal) * 1000:.4f} ms")

    awal = time.time()
    for _ in range(n):
        q.dequeue()
    print(f"  queue dequeue: {(time.time() - awal) * 1000:.4f} ms")

    pohon = BST()
    awal = time.time()
    for x in data:
        pohon.insert(x)
    print(f"  bst insert  : {(time.time() - awal) * 1000:.4f} ms")

    awal = time.time()
    for x in data:
        pohon.search(x)
    print(f"  bst search  : {(time.time() - awal) * 1000:.4f} ms")
    print()