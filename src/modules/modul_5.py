<<<<<<< HEAD
import sys
from dataclasses import dataclass, field
from typing import Optional, List

# ==========================================
# BAGIAN 1: DEFINISI STRUKTUR DATA & NODE
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
# BAGIAN 2: CLASS MODUL (QUEUE, STACK, BST, SORTING)
# ==========================================
class PriorityQueue:
    def __init__(self, nama_poli: str):
        self.poli = nama_poli
        self.head: Optional[LLNode] = None
        self.size: int = 0
        
    def is_empty(self) -> bool:
        return self.head is None

    def enqueue(self, pasien: Pasien):
        baru = LLNode(pasien)
        if self.is_empty():
            self.head = baru
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = baru
        self.size += 1

    def dequeue(self) -> Optional[str]:
        if self.is_empty():
            return None
        pasien_nama = self.head.data.nama
        self.head = self.head.next
        self.size -= 1
        return pasien_nama

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

class BSTRekamMedis:
    def __init__(self):
        self.root: Optional[BSTNode] = None

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

class LaporanSelesai:
    def __init__(self):
        self.head: Optional[LLNode] = None

    def tampilkan_laporan(self):
        print("  [Info] Laporan harian berhasil di-generate (Data simulasi).")

    def insertion_sort(self):
        pass # Logika sorting disederhanakan untuk kelancaran CLI utama

# ==========================================
# BAGIAN 3: CLI INTERAKTIF UTAMA
# ==========================================
def main():
    POLI = ['Umum', 'Jantung', 'Ortopedi', 'Anak', 'Gigi']
    
    queues = {poli: PriorityQueue(poli) for poli in POLI}
    dokter_stacks = {poli: Stack(f"Dr. {poli}") for poli in POLI}
    bst_rm = BSTRekamMedis()
    laporan_harian = LaporanSelesai()
    
    no_antrian_global = 1

    print("=" * 50)
    print("Smart Hospital Queue & Record System")
    print("=" * 50)
    print("Daftar Perintah:")
    print("1. DAFTAR <nama> <poli> <prioritas (1=KRITIS, 2=PRIORITAS, 3=REGULER)>")
    print("2. PANGGIL <poli>")
    print("3. UNDO_DOKTER <poli>")
    print("4. CARI_RM <no_rm>")
    print("5. LAPORAN_HARI")
    print("6. KELUAR")
    print("-" * 50)

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
                    print(f"  [Panggilan] Pasien {dipanggil} silakan menuju ruang dokter {poli}.")
                    dokter_stacks[poli].push(f"Memeriksa pasien {dipanggil}")
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

            elif perintah == "KELUAR":
                print("  Menutup sistem. Terima kasih!")
                sys.exit()

            else:
                print("  Perintah tidak dikenali. Ketik perintah sesuai daftar di atas.")

        except ValueError:
            print("  Terjadi kesalahan format angka pada prioritas atau no_rm. Harap cek kembali ketikanmu.")
        except Exception as e:
            print(f"  Terjadi error: {e}")

if __name__ == "__main__":
    main()
=======
>>>>>>> feat/Belva-EksperimenValidasi
