import sys
import time
import random
from dataclasses import dataclass, field
from typing import Optional, List

# ==========================================
# BAGIAN 1: DEFINISI STRUKTUR DATA UTAMA
# (Gabungan dari Modul 1, 3, dan 4)
# ==========================================
@dataclass
class Pasien:
    no_antrian: int
    nama: str
    poli: str
    prioritas: int
    waktu_daftar: float = 0.0
    waktu_tunggu: float = 0.0

@dataclass
class RekorMedis:
    no_rm: int
    nama: str
    riwayat: List[str] = field(default_factory=list)

class LLNode:
    def __init__(self, data):
        self.data = data
        self.next: Optional['LLNode'] = None

class BSTNode:
    def __init__(self, rekord: RekorMedis):
        self.rekord = rekord
        self.left: Optional['BSTNode'] = None
        self.right: Optional['BSTNode'] = None


# ==========================================
# BAGIAN 2: LOGIKA STRUKTUR DATA
# (Gabungan dari Modul 1, 2, 3, dan 4)
# ==========================================

# -- MODUL 1: Priority Queue --
class PriorityQueue:
    def __init__(self, nama_poli: str = ""):
        self.poli = nama_poli
        self.head: Optional[LLNode] = None
        self.size: int = 0

    def is_empty(self) -> bool:
        return self.head is None

    def enqueue(self, pasien: Pasien):
        baru = LLNode(pasien)
        if self.is_empty():
            self.head = baru
        elif baru.data.prioritas < self.head.data.prioritas:
            # Prioritas 1 (KRITIS) paling depan
            baru.next = self.head
            self.head = baru
        else:
            curr = self.head
            while curr.next and curr.next.data.prioritas <= baru.data.prioritas:
                curr = curr.next
            baru.next = curr.next
            curr.next = baru
        self.size += 1

    def dequeue(self) -> Optional[Pasien]:
        if self.is_empty():
            return None
        pasien = self.head.data
        self.head = self.head.next
        self.size -= 1
        return pasien

# -- MODUL 2: Stack --
class Stack:
    def __init__(self, nama_dokter: str):
        self.nama_dokter = nama_dokter
        self.top: Optional[LLNode] = None
        self._size: int = 0

    def is_empty(self) -> bool:
        return self.top is None

    def push(self, tindakan: str) -> None:
        baru = LLNode(tindakan)
        baru.next = self.top
        self.top = baru
        self._size += 1

    def pop(self) -> Optional[str]:
        if self.is_empty():
            return None
        tindakan = self.top.data
        self.top = self.top.next
        self._size -= 1
        return tindakan

# -- MODUL 3: Binary Search Tree (BST) --
class BSTRekamMedis:
    def __init__(self):
        self.root: Optional[BSTNode] = None

    def insert(self, rekord: RekorMedis):
        if self.root is None:
            self.root = BSTNode(rekord)
            return
        curr = self.root
        while True:
            if rekord.no_rm < curr.rekord.no_rm:
                if curr.left is None:
                    curr.left = BSTNode(rekord)
                    break
                curr = curr.left
            elif rekord.no_rm > curr.rekord.no_rm:
                if curr.right is None:
                    curr.right = BSTNode(rekord)
                    break
                curr = curr.right
            else:
                break

    def search(self, no_rm: int) -> Optional[RekorMedis]:
        curr = self.root
        while curr:
            if no_rm == curr.rekord.no_rm:
                return curr.rekord
            elif no_rm < curr.rekord.no_rm:
                curr = curr.left
            else:
                curr = curr.right
        return None

# -- MODUL 4: Linked List & Insertion Sort --
class LaporanSelesai:
    def __init__(self):
        self.head: Optional[LLNode] = None

    def tambah_pasien_selesai(self, pasien: Pasien):
        baru = LLNode(pasien)
        baru.next = self.head
        self.head = baru

    def insertion_sort(self):
        if self.head is None or self.head.next is None:
            return 
        
        sorted_head = None
        current = self.head

        while current is not None:
            next_node = current.next
            if sorted_head is None:
                current.next = None
                sorted_head = current
            elif (current.data.waktu_tunggu > sorted_head.data.waktu_tunggu) or \
                 (current.data.waktu_tunggu == sorted_head.data.waktu_tunggu and current.data.no_antrian < sorted_head.data.no_antrian):
                current.next = sorted_head
                sorted_head = current
            else:
                search = sorted_head
                while search.next is not None:
                    waktu_lebih_lama = current.data.waktu_tunggu > search.next.data.waktu_tunggu
                    waktu_sama_antrian_kecil = (current.data.waktu_tunggu == search.next.data.waktu_tunggu) and (current.data.no_antrian < search.next.data.no_antrian)
                    if waktu_lebih_lama or waktu_sama_antrian_kecil:
                        break
                    search = search.next
                current.next = search.next
                search.next = current
            current = next_node
        self.head = sorted_head

    def tampilkan_laporan(self):
        if self.head is None:
            print("  Laporan kosong.")
            return

        print(f"  {'No. Antrian':<15} | {'Nama':<15} | {'Waktu Tunggu (menit)':<20}")
        print("  " + "-" * 55)
        curr = self.head
        while curr:
            print(f"  {curr.data.no_antrian:<15} | {curr.data.nama:<15} | {curr.data.waktu_tunggu:<20}")
            curr = curr.next
        print("  " + "-" * 55)


# ==========================================
# BAGIAN 3: SISTEM CLI (MODUL 5)
# ==========================================
def jalankan_sistem_cli():
    POLI = ['Umum', 'Jantung', 'Ortopedi', 'Anak', 'Gigi']
    
    queues = {poli: PriorityQueue(poli) for poli in POLI}
    dokter_stacks = {poli: Stack(f"Dr. {poli}") for poli in POLI}
    bst_rm = BSTRekamMedis()
    laporan_harian = LaporanSelesai()
    
    no_antrian_global = 1

    print("\n" + "=" * 50)
    print("Smart Hospital Queue & Record System - Interaktif")
    print("=" * 50)
    print("Daftar Perintah:")
    print("1. DAFTAR <nama> <poli> <prioritas (1=KRITIS, 2=PRIORITAS, 3=REGULER)>")
    print("2. PANGGIL <poli>")
    print("3. UNDO_DOKTER <poli>")
    print("4. CARI_RM <no_rm>")
    print("5. LAPORAN_HARI")
    print("6. KEMBALI_KE_MENU")
    print("-" * 50)

    # Masukkan beberapa data RM dummy agar fungsi CARI_RM bisa langsung dicoba
    bst_rm.insert(RekorMedis(101, "Siti", ["Cek Jantung"]))
    bst_rm.insert(RekorMedis(105, "Andi", ["Demam"]))

    while True:
        try:
            input_user = input("\nMasukkan perintah> ").strip().split()
            if not input_user:
                continue
                
            perintah = input_user[0].upper()

            if perintah == "DAFTAR":
                if len(input_user) < 4:
                    print("  Format salah! Gunakan: DAFTAR <nama> <poli> <prioritas>")
                    continue
                
                nama = input_user[1]
                poli = input_user[2].capitalize()
                prioritas = int(input_user[3])
                
                if poli not in queues:
                    print(f"  Poli {poli} tidak tersedia. Pilih: {POLI}")
                    continue
                
                print("  [Proses] Big-O operasi DAFTAR (Priority Queue Enqueue): O(n)")
                pasien_baru = Pasien(no_antrian_global, nama, poli, prioritas)
                queues[poli].enqueue(pasien_baru) 
                print(f"  [Berhasil] {nama} berhasil didaftarkan ke antrean {poli} (Antrian #{no_antrian_global})")
                no_antrian_global += 1

            elif perintah == "PANGGIL":
                if len(input_user) < 2:
                    print("  Format salah! Gunakan: PANGGIL <poli>")
                    continue
                
                poli = input_user[1].capitalize()
                if poli not in queues:
                    print(f"  Poli {poli} tidak tersedia.")
                    continue

                print("  [Proses] Big-O operasi PANGGIL (Priority Queue Dequeue): O(1)")
                dipanggil = queues[poli].dequeue()
                
                if dipanggil:
                    print(f"  [Panggilan] Pasien {dipanggil.nama} silakan menuju ruang dokter {poli}.")
                    dokter_stacks[poli].push(f"Memeriksa pasien {dipanggil.nama}")
                    
                    # Simulasikan waktu tunggu acak lalu masukkan ke laporan harian
                    dipanggil.waktu_tunggu = random.randint(10, 60)
                    laporan_harian.tambah_pasien_selesai(dipanggil)
                else:
                    print(f"  Antrean di {poli} saat ini kosong.")

            elif perintah == "UNDO_DOKTER":
                if len(input_user) < 2:
                    print("  Format salah! Gunakan: UNDO_DOKTER <poli>")
                    continue
                
                poli = input_user[1].capitalize()
                if poli not in dokter_stacks:
                    print(f"  Dokter di poli {poli} tidak ditemukan.")
                    continue

                print("  [Proses] Big-O operasi UNDO (Stack Pop): O(1)")
                dibatalkan = dokter_stacks[poli].pop()
                if dibatalkan:
                    print(f"  [Batal] Tindakan dibatalkan: '{dibatalkan}'")
                else:
                    print(f"  Log Dr. {poli} kosong, tidak ada yang bisa di-undo.")

            elif perintah == "CARI_RM":
                if len(input_user) < 2:
                    print("  Format salah! Gunakan: CARI_RM <no_rm>")
                    continue
                
                no_rm = int(input_user[1])
                print("  [Proses] Big-O operasi CARI_RM (BST Search): rata-rata O(log n)")
                hasil = bst_rm.search(no_rm)
                if hasil:
                    print(f"  [Ditemukan] Rekam Medis: {hasil.nama} (RM: {hasil.no_rm}) | Riwayat: {hasil.riwayat}")
                else:
                    print(f"  [Gagal] Rekam Medis dengan nomor {no_rm} tidak ditemukan.")

            elif perintah == "LAPORAN_HARI":
                print("  [Proses] Big-O operasi LAPORAN_HARI (Insertion Sort): O(n^2)")
                laporan_harian.insertion_sort()
                laporan_harian.tampilkan_laporan()

            elif perintah in ["KELUAR", "KEMBALI_KE_MENU"]:
                print("  Kembali ke menu utama.")
                break

            else:
                print("  Perintah tidak dikenali. Ketik perintah sesuai daftar di atas.")

        except ValueError:
            print("  Terjadi kesalahan format angka pada prioritas atau no_rm. Harap cek kembali ketikanmu.")
        except Exception as e:
            print(f"  Terjadi error: {e}")


# ==========================================
# BAGIAN 4: EKSPERIMEN WAKTU (MODUL 6)
# ==========================================
def jalankan_eksperimen():
    # Set seed acak
    random.seed(42)

    POLI = ['Umum', 'Jantung', 'Ortopedi', 'Anak', 'Gigi']
    N_list = [50, 200, 500]
    
    print("\n" + "=" * 75)
    print("Hasil Eksperimen & Validasi Runtime (Seed=42)")
    print("=" * 75)
    print(f"{'N':<5} | {'Enqueue (s)':<15} | {'Dequeue (s)':<15} | {'BST Insert (s)':<15} | {'BST Search (s)':<15}")
    print("-" * 75)

    for n in N_list:
        pq = PriorityQueue()
        bst = BSTRekamMedis()
        
        # Siapkan data acak
        data_pasien = [Pasien(i, f"Pasien{i}", random.choice(POLI), random.randint(1, 3)) for i in range(n)]
        nomor_rm_acak = random.sample(range(1, 10000), n)
        data_rm = [RekorMedis(no, f"Pasien{no}") for no in nomor_rm_acak]

        # 1. Uji Runtime Enqueue
        start_waktu = time.time()
        for p in data_pasien:
            pq.enqueue(p)
        waktu_enqueue = time.time() - start_waktu

        # 2. Uji Runtime Dequeue
        start_waktu = time.time()
        while not pq.is_empty():
            pq.dequeue()
        waktu_dequeue = time.time() - start_waktu

        # 3. Uji Runtime BST Insert
        start_waktu = time.time()
        for rm in data_rm:
            bst.insert(rm)
        waktu_bst_insert = time.time() - start_waktu

        # 4. Uji Runtime BST Search
        start_waktu = time.time()
        for rm in data_rm:
            bst.search(rm.no_rm)
        waktu_bst_search = time.time() - start_waktu

        print(f"{n:<5} | {waktu_enqueue:<15.6f} | {waktu_dequeue:<15.6f} | {waktu_bst_insert:<15.6f} | {waktu_bst_search:<15.6f}")
    
    print("=" * 75)
    print("Catatan: Salin tabel angka di atas untuk dimasukkan ke dalam laporan akhir.")
    input("\nTekan Enter untuk kembali ke menu utama...")


# ==========================================
# BAGIAN 5: MENU UTAMA PENGENDALI
# ==========================================
def main():
    while True:
        print("\n" + "=" * 40)
        print("Sistem Algoritma Rumah Sakit Terpusat")
        print("=" * 40)
        print("1. Jalankan Sistem Antrean CLI (Modul 1-5)")
        print("2. Jalankan Uji Runtime Eksperimen (Modul 6)")
        print("3. Keluar dari Program")
        print("-" * 40)
        
        pilihan = input("Pilih menu (1/2/3): ").strip()
        
        if pilihan == "1":
            jalankan_sistem_cli()
        elif pilihan == "2":
            jalankan_eksperimen()
        elif pilihan == "3":
            print("Program ditutup. Terima kasih!")
            sys.exit()
        else:
            print("Pilihan tidak valid, silakan ketik angka 1, 2, atau 3.")

if __name__ == "__main__":
    main()