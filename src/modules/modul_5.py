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