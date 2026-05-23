from typing import Optional

# Bikin class LLNode langsung di sini biar nggak error nyari file eksternal
class LLNode:
    def __init__(self, data: str):
        self.data = data
        self.next = None

class Stack:
    """
    Stack berbasis Singly Linked List.
    Digunakan untuk mencatat tindakan dokter per sesi.
    Fitur undo bekerja lewat pop() — ambil tindakan terakhir.
    """
    def __init__(self, nama_dokter: str):
        self.nama_dokter = nama_dokter
        self.top: Optional[LLNode] = None
        self._size: int = 0

    def is_empty(self) -> bool:
        return self.top is None

    def __len__(self) -> int:
        return self._size

    def push(self, tindakan: str) -> None:
        baru = LLNode(tindakan)
        baru.next = self.top
        self.top = baru
        self._size += 1

    def pop(self) -> Optional[str]:
        if self.is_empty():
            return None
        tindakan = self.top.data
        self.top = self.top.next
        self._size -= 1
        return tindakan

    def peek(self) -> Optional[str]:
        if self.is_empty():
            return None
        return self.top.data

    def log_all(self) -> None:
        if self.is_empty():
            print(f"  Log {self.nama_dokter}: belum ada tindakan.")
            return
        
        print(f"  Log tindakan Dr. {self.nama_dokter} ({self._size} tindakan):")
        curr = self.top
        urutan = 1
        while curr:
            print(f"    {urutan}. {curr.data}")
            curr = curr.next
            urutan += 1

if __name__ == "__main__":
    s = Stack("Arief")

    tindakan_list = [
        "Periksa tekanan darah",
        "Resepkan parasetamol 500mg",
        "Suntik vitamin B12",
        "Rujuk ke radiologi",
    ]

    for t in tindakan_list:
        s.push(t)
        print(f"  [PUSH] {t}")

    print()
    s.log_all()

    print("\n=== Undo tindakan terakhir ===")
    dibatalkan = s.pop()
    print(f"  Dibatalkan: {dibatalkan}")

    print()
    s.log_all()