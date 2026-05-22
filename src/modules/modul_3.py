from dataclasses import dataclass, field

@dataclass
class RekorMedis:
    no_rm: int
    nama: str
    riwayat: list = field(default_factory=list)

class BSTNode:
    def __init__(self, rekord: RekorMedis):
        self.rekord = rekord
        self.left = None
        self.right = None

class BSTRekamMedis:
    def __init__(self):
        self.root = None

    def insert(self, rekord: RekorMedis):
        if self.root is None:
            self.root = BSTNode(rekord)
            return
            
        curr = self.root
        while True:
            if rekord.no_rm < curr.rekord.no_rm:
                if curr.left is None:
                    curr.left = BSTNode(rekord)
                    break
                curr = curr.left
            elif rekord.no_rm > curr.rekord.no_rm:
                if curr.right is None:
                    curr.right = BSTNode(rekord)
                    break
                curr = curr.right
            else:
                break # Jika no_rm sudah ada, abaikan

    def search(self, no_rm: int):
        curr = self.root
        while curr is not None:
            if no_rm == curr.rekord.no_rm:
                return curr.rekord
            elif no_rm < curr.rekord.no_rm:
                curr = curr.left
            else:
                curr = curr.right
        return None