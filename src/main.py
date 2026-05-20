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


class Node:
    def __init__(self, no_rm, data):
        self.no_rm = no_rm
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, no_rm, data):
        baru = Node(no_rm, data)
        if self.root is None:
            self.root = baru
            return
        curr = self.root
        while True:
            if no_rm < curr.no_rm:
                if curr.left is None:
                    curr.left = baru
                    break
                curr = curr.left
            elif no_rm > curr.no_rm:
                if curr.right is None:
                    curr.right = baru
                    break
                curr = curr.right
            else:
                print("no rm sudah ada")
                break

    def search(self, no_rm):
        curr = self.root
        while curr:
            if no_rm == curr.no_rm:
                return curr.data
            elif no_rm < curr.no_rm:
                curr = curr.left
            else:
                curr = curr.right
        return "tidak ditemukan"

    def delete(self, no_rm):
        self.root = self._delete(self.root, no_rm)

    def _delete(self, node, no_rm):
        if node is None:
            return None
        if no_rm < node.no_rm:
            node.left = self._delete(node.left, no_rm)
        elif no_rm > node.no_rm:
            node.right = self._delete(node.right, no_rm)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_node = node.right
            while min_node.left:
                min_node = min_node.left
            node.no_rm = min_node.no_rm
            node.data = min_node.data
            node.right = self._delete(node.right, min_node.no_rm)
        return node

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(f"  no rm {node.no_rm}: {node.data}")
            self.inorder(node.right)


rm = BST()
rm.insert(103, "Budi | umur: 45 | diagnosis: hipertensi")
rm.insert(101, "Siti | umur: 30 | diagnosis: flu")
rm.insert(105, "Andi | umur: 52 | diagnosis: diabetes")
rm.insert(102, "Rudi | umur: 27 | diagnosis: tipes")
rm.insert(104, "Wati | umur: 38 | diagnosis: asma")

print("semua rekam medis:")
rm.inorder(rm.root)

print("\ncari no rm 102:")
print(" ", rm.search(102))

print("\ncari no rm 999:")
print(" ", rm.search(999))

print("\nhapus no rm 101")
rm.delete(101)
print("rekam medis setelah dihapus:")
rm.inorder(rm.root)


class Node:
    def __init__(self, nama, waktu_tunggu, no_antrian):
        self.nama = nama
        self.waktu_tunggu = waktu_tunggu
        self.no_antrian = no_antrian
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def tambah(self, nama, waktu_tunggu, no_antrian):
        baru = Node(nama, waktu_tunggu, no_antrian)
        if self.head is None:
            self.head = baru
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = baru

    def tampil(self):
        curr = self.head
        while curr:
            print(f"  {curr.nama} | tunggu: {curr.waktu_tunggu} menit | no: {curr.no_antrian}")
            curr = curr.next

    def insertion_sort_waktu(self):
        if self.head is None:
            return
        sorted_head = None
        curr = self.head
        while curr:
            next_node = curr.next
            sorted_head = self._insert_sorted(sorted_head, curr)
            curr = next_node
        self.head = sorted_head

    def _insert_sorted(self, sorted_head, baru):
        baru.next = None
        if sorted_head is None or baru.waktu_tunggu > sorted_head.waktu_tunggu:
            baru.next = sorted_head
            return baru
        curr = sorted_head
        while curr.next and curr.next.waktu_tunggu >= baru.waktu_tunggu:
            curr = curr.next
        baru.next = curr.next
        curr.next = baru
        return sorted_head

    def selection_sort_antrian(self):
        curr = self.head
        while curr:
            min_node = curr
            cari = curr.next
            while cari:
                if cari.no_antrian < min_node.no_antrian:
                    min_node = cari
                cari = cari.next
            curr.nama, min_node.nama = min_node.nama, curr.nama
            curr.waktu_tunggu, min_node.waktu_tunggu = min_node.waktu_tunggu, curr.waktu_tunggu
            curr.no_antrian, min_node.no_antrian = min_node.no_antrian, curr.no_antrian
            curr = curr.next


laporan = LinkedList()
laporan.tambah("Budi", 45, 3)
laporan.tambah("Siti", 20, 1)
laporan.tambah("Andi", 60, 5)
laporan.tambah("Rudi", 35, 2)
laporan.tambah("Wati", 50, 4)

print("data awal:")
laporan.tampil()

laporan.insertion_sort_waktu()
print("\nsetelah insertion sort (waktu tunggu terlama dulu):")
laporan.tampil()

laporan.selection_sort_antrian()
print("\nsetelah selection sort (no antrian urut):")
laporan.tampil()


class Node:
    def __init__(self, nama, prioritas):
        self.nama = nama
        self.prioritas = prioritas
        self.next = None

class NodeStack:
    def __init__(self, tindakan):
        self.tindakan = tindakan
        self.next = None

class NodeBST:
    def __init__(self, no_rm, data):
        self.no_rm = no_rm
        self.data = data
        self.left = None
        self.right = None


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
            return None
        nama = self.head.nama
        self.head = self.head.next
        return nama

    def tampil(self):
        if self.is_empty():
            print(f"  {self.poli}: kosong")
            return
        curr = self.head
        hasil = []
        while curr:
            hasil.append(f"{curr.nama}({curr.prioritas})")
            curr = curr.next
        print(f"  {self.poli}: {' -> '.join(hasil)}")


class Stack:
    def __init__(self, nama):
        self.nama = nama
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, tindakan):
        baru = NodeStack(tindakan)
        baru.next = self.top
        self.top = baru

    def pop(self):
        if self.is_empty():
            return None
        t = self.top.tindakan
        self.top = self.top.next
        return t

    def log_all(self):
        if self.is_empty():
            print(f"  {self.nama}: belum ada tindakan")
            return
        curr = self.top
        print(f"  log {self.nama}:")
        while curr:
            print(f"    - {curr.tindakan}")
            curr = curr.next


class BST:
    def __init__(self):
        self.root = None

    def insert(self, no_rm, data):
        baru = NodeBST(no_rm, data)
        if self.root is None:
            self.root = baru
            return
        curr = self.root
        while True:
            if no_rm < curr.no_rm:
                if curr.left is None:
                    curr.left = baru
                    break
                curr = curr.left
            elif no_rm > curr.no_rm:
                if curr.right is None:
                    curr.right = baru
                    break
                curr = curr.right
            else:
                print("no rm sudah ada")
                break

    def search(self, no_rm):
        curr = self.root
        while curr:
            if no_rm == curr.no_rm:
                return curr.data
            elif no_rm < curr.no_rm:
                curr = curr.left
            else:
                curr = curr.right
        return None

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(f"  {node.no_rm}: {node.data}")
            self.inorder(node.right)


poli_list = {
    "umum"   : PriorityQueue("poli umum"),
    "anak"   : PriorityQueue("poli anak"),
    "gigi"   : PriorityQueue("poli gigi"),
    "jantung": PriorityQueue("poli jantung"),
    "mata"   : PriorityQueue("poli mata"),
}

dokter_list = {
    "d1": Stack("dr. Tirta"),
    "d2": Stack("dr. Gia"),
}

rekam_medis = BST()
rekam_medis.insert(101, "Budi | umur: 45 | hipertensi")
rekam_medis.insert(102, "Siti | umur: 30 | flu")

laporan_hari = []

print("selamat datang di sistem antrian klinik")
print("perintah: DAFTAR / PANGGIL / UNDO_DOKTER / CARI_RM / TAMBAH_RM / LAPORAN_HARI / KELUAR")

while True:
    perintah = input("\n>> ").strip().split()
    if not perintah:
        continue

    cmd = perintah[0].upper()

    if cmd == "DAFTAR":
        if len(perintah) < 4:
            print("contoh: DAFTAR Budi umum NORMAL")
            continue
        nama      = perintah[1]
        poli      = perintah[2].lower()
        prioritas = perintah[3].upper()
        if poli not in poli_list:
            print(f"poli {poli} tidak ada")
            continue
        poli_list[poli].enqueue(nama, prioritas)
        print(f"{nama} masuk antrian {poli} sebagai {prioritas}")
        print("big-o: O(n)")

    elif cmd == "PANGGIL":
        if len(perintah) < 2:
            print("contoh: PANGGIL umum")
            continue
        poli = perintah[1].lower()
        if poli not in poli_list:
            print(f"poli {poli} tidak ada")
            continue
        pasien = poli_list[poli].dequeue()
        if pasien:
            print(f"{pasien} dipanggil dari {poli}")
            laporan_hari.append(pasien)
            dokter_list["d1"].push(f"menangani {pasien}")
        else:
            print(f"antrian {poli} kosong")
        print("big-o: O(1)")

    elif cmd == "UNDO_DOKTER":
        if len(perintah) < 2:
            print("contoh: UNDO_DOKTER d1")
            continue
        id_dokter = perintah[1].lower()
        if id_dokter not in dokter_list:
            print(f"id dokter {id_dokter} tidak ada")
            continue
        hasil = dokter_list[id_dokter].pop()
        if hasil:
            print(f"tindakan dibatalkan: {hasil}")
        else:
            print("belum ada tindakan")
        print("big-o: O(1)")

    elif cmd == "CARI_RM":
        if len(perintah) < 2:
            print("contoh: CARI_RM 101")
            continue
        no_rm = int(perintah[1])
        hasil = rekam_medis.search(no_rm)
        if hasil:
            print(f"ketemu -> {hasil}")
        else:
            print(f"no rm {no_rm} tidak ada")
        print("big-o: rata-rata O(log n), worst case O(n)")

    elif cmd == "TAMBAH_RM":
        if len(perintah) < 3:
            print("contoh: TAMBAH_RM 103 Andi umur:27 tipes")
            continue
        no_rm = int(perintah[1])
        data  = " ".join(perintah[2:])
        rekam_medis.insert(no_rm, data)
        print(f"rekam medis {no_rm} berhasil disimpan")
        print("big-o: rata-rata O(log n), worst case O(n)")

    elif cmd == "LAPORAN_HARI":
        print("pasien yang sudah ditangani:")
        if not laporan_hari:
            print("  belum ada")
        else:
            for i, p in enumerate(laporan_hari, 1):
                print(f"  {i}. {p}")
        print("\nantrian per poli:")
        for p in poli_list.values():
            p.tampil()
        print("\nrekam medis:")
        rekam_medis.inorder(rekam_medis.root)
        print("\nlog dokter:")
        for d in dokter_list.values():
            d.log_all()

    elif cmd == "KELUAR":
        print("sistem ditutup")
        break

    else:
        print(f"perintah {cmd} tidak dikenal")


import time
import random


class Node:
    def __init__(self, nama, prioritas):
        self.nama = nama
        self.prioritas = prioritas
        self.next = None

class NodeBST:
    def __init__(self, no_rm, data):
        self.no_rm = no_rm
        self.data = data
        self.left = None
        self.right = None


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
            return None
        nama = self.head.nama
        self.head = self.head.next
        return nama

    def hitung(self):
        n = 0
        curr = self.head
        while curr:
            n += 1
            curr = curr.next
        return n


class BST:
    def __init__(self):
        self.root = None

    def insert(self, no_rm, data):
        baru = NodeBST(no_rm, data)
        if self.root is None:
            self.root = baru
            return
        curr = self.root
        while True:
            if no_rm < curr.no_rm:
                if curr.left is None:
                    curr.left = baru
                    break
                curr = curr.left
            elif no_rm > curr.no_rm:
                if curr.right is None:
                    curr.right = baru
                    break
                curr = curr.right
            else:
                break

    def search(self, no_rm):
        curr = self.root
        while curr:
            if no_rm == curr.no_rm:
                return curr.data
            elif no_rm < curr.no_rm:
                curr = curr.left
            else:
                curr = curr.right
        return None

    def hitung(self):
        return self._hitung(self.root)

    def _hitung(self, node):
        if node is None:
            return 0
        return 1 + self._hitung(node.left) + self._hitung(node.right)


nama_pasien = ["Budi", "Siti", "Andi", "Rudi", "Wati",
               "Hasan", "Dewi", "Fajar", "Rina", "Tono"]
poli_nama   = ["umum", "anak", "gigi", "jantung", "mata"]
pri_list    = ["NORMAL", "NORMAL", "NORMAL", "KRITIS"]

random.seed(42)
ukuran = [50, 200, 500]

hasil_enqueue = []
hasil_dequeue = []
hasil_insert  = []
hasil_search  = []

for n in ukuran:
    data_pasien = [(random.choice(nama_pasien) + str(i),
                    random.choice(poli_nama),
                    random.choice(pri_list)) for i in range(n)]

    queues = {p: PriorityQueue(p) for p in poli_nama}

    awal = time.time()
    for nama, poli, pri in data_pasien:
        queues[poli].enqueue(nama, pri)
    t_enqueue = (time.time() - awal) * 1000

    awal = time.time()
    for poli in queues:
        while not queues[poli].is_empty():
            queues[poli].dequeue()
    t_dequeue = (time.time() - awal) * 1000

    bst = BST()
    no_rm_list = random.sample(range(1000, 9999), n)

    awal = time.time()
    for i, no_rm in enumerate(no_rm_list):
        bst.insert(no_rm, f"pasien_{i}")
    t_insert = (time.time() - awal) * 1000

    awal = time.time()
    for no_rm in no_rm_list:
        bst.search(no_rm)
    t_search = (time.time() - awal) * 1000

    hasil_enqueue.append(t_enqueue)
    hasil_dequeue.append(t_dequeue)
    hasil_insert.append(t_insert)
    hasil_search.append(t_search)

    print(f"n = {n}")
    print(f"  enqueue   : {t_enqueue:.4f} ms")
    print(f"  dequeue   : {t_dequeue:.4f} ms")
    print(f"  bst insert: {t_insert:.4f} ms")
    print(f"  bst search: {t_search:.4f} ms")
    print()

# konfirmasi struktur
random.seed(42)
queues = {p: PriorityQueue(p) for p in poli_nama}
bst    = BST()

for i in range(10):
    nama = random.choice(nama_pasien) + str(i)
    poli = random.choice(poli_nama)
    pri  = random.choice(pri_list)
    queues[poli].enqueue(nama, pri)
    bst.insert(1000 + i, f"{nama} | poli: {poli}")

print("isi queue per poli:")
for p in queues:
    print(f"  {p}: {queues[p].hitung()} pasien")
print(f"bst: {bst.hitung()} data tersimpan")

# Rangkuman Tren Performa dalam Bentuk Tabel
print("\n" + "="*75)
print(f"{'Jumlah Pasien (n)':<18} | {'Enqueue (ms)':<12} | {'Dequeue (ms)':<12} | {'BST Insert (ms)':<15} | {'BST Search (ms)':<15}")
print("="*75)
for i in range(len(ukuran)):
    print(f"{ukuran[i]:<18} | {hasil_enqueue[i]:<12.4f} | {hasil_dequeue[i]:<12.4f} | {hasil_insert[i]:<15.4f} | {hasil_search[i]:<15.4f}")
print("="*75)