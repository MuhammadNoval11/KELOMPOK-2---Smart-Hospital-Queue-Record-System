from src.data_structures.linked_list import LLNode, Pasien
class PriorityQueue:
    """Priority Queue berbasis Singly Linked List, terurut prioritas ASC."""
    def __init__(self, nama_poli: str):
        self.poli = nama_poli
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def enqueue(self, pasien: Pasien):
        """Big-O: O(n) worst-case"""
        baru = LLNode(pasien)
        
        # Jika kosong atau prioritas lebih tinggi (angka lebih kecil)
        if self.is_empty() or pasien.prioritas < self.head.data.prioritas:
            baru.next = self.head
            self.head = baru
        else:
            # Cari posisi yang tepat (Tie-break FIFO)
            curr = self.head
            while curr.next is not None and curr.next.data.prioritas <= pasien.prioritas:
                curr = curr.next
            baru.next = curr.next
            curr.next = baru
            
        self.size += 1

    def dequeue(self):
        """Big-O: O(1)"""
        if self.is_empty():
            return None
        data_diambil = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data_diambil

    def peek(self):
        """Big-O: O(1)"""
        if self.is_empty():
            return None
        return self.head.data