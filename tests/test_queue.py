class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return "Queue kosong"

    def is_empty(self):
        return len(self.items) == 0

    def tampil(self):
        print(self.items)
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.tampil()
print(q.dequeue())
q.tampil()