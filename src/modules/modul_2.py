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
<<<<<<< HEAD
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
=======
            print(f"   - {curr.data}")
            curr = curr.next
>>>>>>> dev
