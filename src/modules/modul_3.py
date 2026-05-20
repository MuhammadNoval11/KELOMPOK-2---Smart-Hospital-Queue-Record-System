<<<<<<< HEAD
=======
class Node:
    def __init__(self, no_rm, data):
        self.no_rm = no_rm
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, no_rm, data):
        baru = Node(no_rm, data)
        if self.root is None:
            self.root = baru
            return
        curr = self.root
        while True:
            if no_rm < curr.no_rm:
                if curr.left is None:
                    curr.left = baru
                    break
                curr = curr.left
            elif no_rm > curr.no_rm:
                if curr.right is None:
                    curr.right = baru
                    break
                curr = curr.right
            else:
                print("no rm sudah ada")
                break

    def search(self, no_rm):
        curr = self.root
        while curr:
            if no_rm == curr.no_rm:
                return curr.data
            elif no_rm < curr.no_rm:
                curr = curr.left
            else:
                curr = curr.right
        return "tidak ditemukan"

    def delete(self, no_rm):
        self.root = self._delete(self.root, no_rm)

    def _delete(self, node, no_rm):
        if node is None:
            return None
        if no_rm < node.no_rm:
            node.left = self._delete(node.left, no_rm)
        elif no_rm > node.no_rm:
            node.right = self._delete(node.right, no_rm)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_node = node.right
            while min_node.left:
                min_node = min_node.left
            node.no_rm = min_node.no_rm
            node.data = min_node.data
            node.right = self._delete(node.right, min_node.no_rm)
        return node

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(f"  no rm {node.no_rm}: {node.data}")
            self.inorder(node.right)


rm = BST()
rm.insert(103, "Budi | umur: 45 | diagnosis: hipertensi")
rm.insert(101, "Siti | umur: 30 | diagnosis: flu")
rm.insert(105, "Andi | umur: 52 | diagnosis: diabetes")
rm.insert(102, "Rudi | umur: 27 | diagnosis: tipes")
rm.insert(104, "Wati | umur: 38 | diagnosis: asma")

print("semua rekam medis:")
rm.inorder(rm.root)

print("\ncari no rm 102:")
print(" ", rm.search(102))

print("\ncari no rm 999:")
print(" ", rm.search(999))

print("\nhapus no rm 101")
rm.delete(101)
print("rekam medis setelah dihapus:")
rm.inorder(rm.root)
>>>>>>> feat/habibi-BTS
