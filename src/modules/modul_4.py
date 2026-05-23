from dataclasses import dataclass
from typing import Optional

# 1. Struktur Data Pasien (Diambil dari template PDF)
@dataclass
class Pasien:
    no_antrian: int
    nama: str
    poli: str
    prioritas: int
    waktu_daftar: float = 0.0
    waktu_tunggu: float = 0.0

# 2. Struktur Node Linked List
class LLNode:
    def __init__(self, data: Pasien):
        self.data = data
        self.next: Optional['LLNode'] = None

# 3. Class untuk Laporan dan Sorting
class LaporanSelesai:
    def __init__(self):
        self.head: Optional[LLNode] = None

    def tambah_pasien_selesai(self, pasien: Pasien):
        """Menambahkan pasien ke daftar riwayat (tanpa urutan)."""
        baru = LLNode(pasien)
        baru.next = self.head
        self.head = baru

    def insertion_sort(self):
        """
        Mengurutkan daftar pasien selesai langsung pada Linked List.
        Big-O: O(n^2).
        Kriteria: 
        1. waktu_tunggu DESC (paling lama di atas)
        2. no_antrian ASC (nomor kecil di atas jika waktu tunggu sama)
        """
        if self.head is None or self.head.next is None:
            return  # Tidak perlu diurutkan jika kosong atau cuma 1 data
        
        sorted_head = None
        current = self.head

        while current is not None:
            next_node = current.next
            
            # Kondisi 1: List yang sudah diurutkan masih kosong
            if sorted_head is None:
                current.next = None
                sorted_head = current
                
            # Kondisi 2: Sisipkan di posisi paling depan (Head baru)
            elif (current.data.waktu_tunggu > sorted_head.data.waktu_tunggu) or \
                 (current.data.waktu_tunggu == sorted_head.data.waktu_tunggu and current.data.no_antrian < sorted_head.data.no_antrian):
                current.next = sorted_head
                sorted_head = current
                
            # Kondisi 3: Cari posisi yang tepat di tengah atau akhir
            else:
                search = sorted_head
                while search.next is not None:
                    # Cek apakah posisi current seharusnya di antara search dan search.next
                    waktu_lebih_lama = current.data.waktu_tunggu > search.next.data.waktu_tunggu
                    waktu_sama_antrian_kecil = (current.data.waktu_tunggu == search.next.data.waktu_tunggu) and (current.data.no_antrian < search.next.data.no_antrian)
                    
                    if waktu_lebih_lama or waktu_sama_antrian_kecil:
                        break
                    search = search.next
                
                # Sisipkan node
                current.next = search.next
                search.next = current
                
            current = next_node
        
        # Perbarui head dengan list yang sudah terurut
        self.head = sorted_head

    def tampilkan_laporan(self):
        """Mencetak laporan ke terminal."""
        if self.head is None:
            print("  Laporan kosong.")
            return

        print(f"{'No. Antrian':<15} | {'Nama':<15} | {'Waktu Tunggu (menit)':<20}")
        print("-" * 55)
        curr = self.head
        while curr:
            print(f"{curr.data.no_antrian:<15} | {curr.data.nama:<15} | {curr.data.waktu_tunggu:<20}")
            curr = curr.next
        print("-" * 55)

# ==========================================
# Blok Eksekusi (Uji Coba Standalone)
# ==========================================
if __name__ == "__main__":
    laporan = LaporanSelesai()

    # Membuat data pasien tiruan
    p1 = Pasien(no_antrian=1, nama="Budi", poli="Umum", prioritas=3, waktu_tunggu=15.0)
    p2 = Pasien(no_antrian=2, nama="Siti", poli="Jantung", prioritas=1, waktu_tunggu=45.0)
    p3 = Pasien(no_antrian=3, nama="Agus", poli="Gigi", prioritas=3, waktu_tunggu=15.0)
    p4 = Pasien(no_antrian=4, nama="Dina", poli="Anak", prioritas=2, waktu_tunggu=30.0)

    # Memasukkan secara acak
    laporan.tambah_pasien_selesai(p1)
    laporan.tambah_pasien_selesai(p4)
    laporan.tambah_pasien_selesai(p2)
    laporan.tambah_pasien_selesai(p3)

    print("=== Laporan SEBELUM Diurutkan ===")
    laporan.tampilkan_laporan()

    # Menjalankan proses sorting
    laporan.insertion_sort()

    print("\n=== Laporan SETELAH Diurutkan ===")
    laporan.tampilkan_laporan()