from modul_1 import LLNode, Pasien

class LaporanSelesai:
    def __init__(self): self.head = None

    def tambah_selesai(self, pasien: Pasien):
        baru = LLNode(pasien)
        baru.next = self.head
        self.head = baru

    def sort_berdasarkan_no_antrian(self):
        curr1 = self.head
        while curr1:
            node_min = curr1
            curr2 = curr1.next
            while curr2:
                if curr2.data.no_antrian < node_min.data.no_antrian: node_min = curr2
                curr2 = curr2.next
            curr1.data, node_min.data = node_min.data, curr1.data
            curr1 = curr1.next