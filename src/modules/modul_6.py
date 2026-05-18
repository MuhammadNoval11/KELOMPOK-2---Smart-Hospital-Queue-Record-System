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

# grafik tren
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
plt.plot(ukuran, hasil_enqueue, marker='o', label='enqueue')
plt.plot(ukuran, hasil_dequeue, marker='o', label='dequeue')
plt.plot(ukuran, hasil_insert,  marker='o', label='bst insert')
plt.plot(ukuran, hasil_search,  marker='o', label='bst search')

plt.xlabel('jumlah pasien (n)')
plt.ylabel('waktu (ms)')
plt.title('grafik tren runtime')
plt.legend()
plt.tight_layout()
plt.savefig('grafik_tren.png')
plt.show()
print("grafik disimpan sebagai grafik_tren.png")