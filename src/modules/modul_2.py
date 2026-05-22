from modul_1 import LLNode

class Stack:
    def __init__(self, nama_dokter):
        self.nama_dokter = nama_dokter
        self.top = None

    def push(self, tindakan: str):
        baru = LLNode(tindakan)
        baru.next = self.top
        self.top = baru

    def pop(self):
        if self.top is None: return None
        ambil = self.top.data
        self.top = self.top.next
        return ambil

    def log_all(self):
        curr = self.top
        while curr:
            print(f"   - {curr.data}")
            curr = curr.next