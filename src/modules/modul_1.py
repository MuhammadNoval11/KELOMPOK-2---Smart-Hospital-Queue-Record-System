# priority queue pake linked list
# buat 5 poli

class Node:
    def __init__(self, nama, prioritas):
        self.nama = nama
        self.prioritas = prioritas
        self.next = None


class PriorityQueue:
    def __init__(self, poli):
        self.poli = poli
        self.head = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, nama, prioritas):
        baru = Node(nama, prioritas)

        if self.is_empty():
            self.head = baru
            return

        if prioritas == "KRITIS":
            if self.head.prioritas != "KRITIS":
                baru.next = self.head
                self.head = baru
            else:
                curr = self.head
                while curr.next and curr.next.prioritas == "KRITIS":
                    curr = curr.next
                baru.next = curr.next
                curr.next = baru
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = baru

    def dequeue(self):
        if self.is_empty():
            return "antrian kosong"
        nama = self.head.nama
        self.head = self.head.next
        return nama

    def peek(self):
        if self.is_empty():
            return "antrian kosong"
        return self.head.nama

    def tampil(self):
        if self.is_empty():
            print(f"{self.poli} : kosong")
            return
        curr = self.head
        hasil = []
        while curr:
            hasil.append(f"{curr.nama}({curr.prioritas})")
            curr = curr.next
        print(f"{self.poli} : {' -> '.join(hasil)}")


# bikin 5 poli
umum    = PriorityQueue("Poli Umum")
anak    = PriorityQueue("Poli Anak")
gigi    = PriorityQueue("Poli Gigi")
jantung = PriorityQueue("Poli Jantung")
mata    = PriorityQueue("Poli Mata")

# daftarin pasien
umum.enqueue("Budi", "NORMAL")
umum.enqueue("Siti", "NORMAL")
umum.enqueue("Andi", "KRITIS")
umum.enqueue("Rudi", "KRITIS")

anak.enqueue("Dani", "NORMAL")
anak.enqueue("Lisa", "KRITIS")

jantung.enqueue("Hasan", "NORMAL")
jantung.enqueue("Wati", "KRITIS")

print("antrian semua poli:")
umum.tampil()
anak.tampil()
gigi.tampil()
jantung.tampil()
mata.tampil()

print("\npanggil pasien poli umum:")
print("dipanggil:", umum.dequeue())
print("dipanggil:", umum.dequeue())
umum.tampil()

print("\nberikutnya di poli anak:", anak.peek())