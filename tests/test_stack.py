from src.data_structures.linked_list import LLNode, Pasien
class Stack:
    """Stack berbasis Singly Linked List untuk log tindakan dokter."""
    def __init__(self, nama_dokter: str):
        self.nama_dokter = nama_dokter
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.top is None

    def push(self, tindakan: str):
        """Big-O: O(1)"""
        baru = LLNode(tindakan)
        baru.next = self.top
        self.top = baru
        self.size += 1

    def pop(self):
        """Big-O: O(1)"""
        if self.is_empty():
            return None
        tindakan_dihapus = self.top.data
        self.top = self.top.next
        self.size -= 1
        return tindakan_dihapus

    def log_all(self):
        if self.is_empty():
            print(f"Log {self.nama_dokter}: Belum ada tindakan.")
            return
        
        print(f"Log {self.nama_dokter}:")
        curr = self.top
        while curr:
            print(f"  - {curr.data}")
            curr = curr.next
            