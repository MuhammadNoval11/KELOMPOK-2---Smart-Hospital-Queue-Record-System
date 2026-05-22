import time
from dataclasses import dataclass, field

@dataclass
class Pasien:
    no_antrian: int
    nama: str
    poli: str
    prioritas: int  # 1-KRITIS, 2-PRIORITAS, 3-REGULER
    waktu_daftar: float = field(default_factory=time.time)
    waktu_tunggu: float = 0.0

class LLNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class PriorityQueue:
    def __init__(self, nama_poli):
        self.poli = nama_poli
        self.head = None
        self.size = 0

    def is_empty(self): return self.head is None

    def enqueue(self, pasien: Pasien):
        baru = LLNode(pasien)
        if self.is_empty() or pasien.prioritas < self.head.data.prioritas:
            baru.next = self.head
            self.head = baru
        else:
            curr = self.head
            while curr.next and curr.next.data.prioritas <= pasien.prioritas:
                curr = curr.next
            baru.next = curr.next
            curr.next = baru
        self.size += 1

    def dequeue(self):
        if self.is_empty(): return None
        ambil = self.head.data
        self.head = self.head.next
        self.size -= 1
        return ambil