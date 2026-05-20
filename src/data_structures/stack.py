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

    def tampil(self):
        print(self.items)


s = Stack()
s.push(5)
s.push(10)
s.push(15)
s.tampil()        
print(s.pop())   
print(s.peek())