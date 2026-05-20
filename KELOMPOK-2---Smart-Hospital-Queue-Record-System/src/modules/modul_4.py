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