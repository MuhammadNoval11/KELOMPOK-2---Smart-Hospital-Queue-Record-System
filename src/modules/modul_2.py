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


dokter_andi = Stack("dr. Andi")
dokter_siti = Stack("dr. Siti")

dokter_andi.push("cek tensi pasien Budi")
dokter_andi.push("kasih resep obat")
dokter_andi.push("rujuk ke poli jantung")

dokter_siti.push("cek gula darah")
dokter_siti.push("suntik insulin")

print("log semua dokter:")
dokter_andi.log_all()
dokter_siti.log_all()

print("\ntindakan terakhir dr. Andi:", dokter_andi.peek())

print("\nundo tindakan dr. Andi:")
print("dihapus:", dokter_andi.pop())
dokter_andi.log_all()

print("\nundo tindakan dr. Siti:")
print("dihapus:", dokter_siti.pop())
dokter_siti.log_all()