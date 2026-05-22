

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

    def inorder(self, node):
        if node:
            self.inorder(node.kiri)
            print(node.data, end=" ")
            self.inorder(node.kanan)


pohon = BST()
pohon.insert(50)
pohon.insert(30)
pohon.insert(70)
pohon.insert(20)
pohon.insert(40)

pohon.inorder(pohon.root)
print()
print(pohon.search(30))
print(pohon.search(99))