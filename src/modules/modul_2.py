class Node:
    def __init__(self, tindakan):
        self.tindakan = tindakan
        self.next = None


class Stack:
    def __init__(self, nama):
        self.nama = nama
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, tindakan):
        baru = Node(tindakan)
        baru.next = self.top
        self.top = baru

    def pop(self):
        if self.is_empty():
            return "stack kosong"
        t = self.top.tindakan
        self.top = self.top.next
        return t

    def peek(self):
        if self.is_empty():
            return "stack kosong"
        return self.top.tindakan

    def log_all(self):
        if self.is_empty():
            print(f"{self.nama}: belum ada tindakan")
            return
        curr = self.top
        print(f"log {self.nama}:")
        while curr:
            print(f"  - {curr.tindakan}")
            curr = curr.next


dokter_tirta = Stack("dr. Tirta")
dokter_gia = Stack("dr. Gia")

dokter_tirta.push("cek tensi pasien Budi")
dokter_tirta.push("kasih resep obat")
dokter_tirta.push("rujuk ke poli jantung")

dokter_gia.push("cek gula darah")
dokter_gia.push("suntik insulin")

print("log semua dokter:")
dokter_tirta.log_all()
dokter_gia.log_all()

print("\ntindakan terakhir dr. Tirta:", dokter_tirta.peek())

print("\nundo tindakan dr. Tirta:")
print("dihapus:", dokter_tirta.pop())
dokter_tirta.log_all()

print("\nundo tindakan dr. Gia:")
print("dihapus:", dokter_gia.pop())
dokter_gia.log_all()