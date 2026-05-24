import time
import random
# import numpy as np
from dataclasses import dataclass, field
from typing import Optional, List

# 1. Set seed acak sesuai kewajiban di panduan agar hasil bisa direproduksi
# np.random.seed(42)
random.seed(42)

# ==========================================
# CLASS STRUKTUR DATA (Disederhanakan untuk Pengujian)
# ==========================================
@dataclass
class Pasien:
    no_antrian: int
    nama: str
    poli: str
    prioritas: int

@dataclass
class RekorMedis:
    no_rm: int
    nama: str
    riwayat: List[str] = field(default_factory=list)

class LLNode:
    def __init__(self, data):
        self.data = data
        self.next: Optional['LLNode'] = None

class PriorityQueue:
    def __init__(self):
        self.head: Optional[LLNode] = None

    def is_empty(self) -> bool:
        return self.head is None

    def enqueue(self, pasien: Pasien):
        baru = LLNode(pasien)
        if self.is_empty():
            self.head = baru
            return
        
        # Logika prioritas: 1 (KRITIS) paling depan
        if baru.data.prioritas < self.head.data.prioritas:
            baru.next = self.head
            self.head = baru
        else:
            curr = self.head
            while curr.next and curr.next.data.prioritas <= baru.data.prioritas:
                curr = curr.next
            baru.next = curr.next
            curr.next = baru

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.head.data
        self.head = self.head.next
        return data

class BSTNode:
    def __init__(self, rekord: RekorMedis):
        self.rekord = rekord
        self.left: Optional['BSTNode'] = None
        self.right: Optional['BSTNode'] = None

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

    def search(self, no_rm: int):
        curr = self.root
        while curr:
            if no_rm == curr.rekord.no_rm:
                return curr.rekord
            elif no_rm < curr.rekord.no_rm:
                curr = curr.left
            else:
                curr = curr.right
        return None

# ==========================================
# FUNGSI EKSPERIMEN & VALIDASI
# ==========================================
def jalankan_eksperimen():
    POLI = ['Umum', 'Jantung', 'Ortopedi', 'Anak', 'Gigi']
    N_list = [50, 200, 500]
    
    print("=" * 75)
    print("Hasil Eksperimen & Validasi Runtime (Seed=42)")
    print("=" * 75)
    print(f"{'N':<5} | {'Enqueue (s)':<15} | {'Dequeue (s)':<15} | {'BST Insert (s)':<15} | {'BST Search (s)':<15}")
    print("-" * 75)

    for n in N_list:
        pq = PriorityQueue()
        bst = BSTRekamMedis()
        
        # Siapkan N data pasien dan N data rekam medis acak
        data_pasien = [Pasien(i, f"Pasien{i}", random.choice(POLI), random.randint(1, 3)) for i in range(n)]
        
        # Acak nomor RM agar BST tidak menjadi garis lurus (skewed)
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

        # 4. Uji Runtime BST Search (Mencari semua data yang ada)
        start_waktu = time.time()
        for rm in data_rm:
            bst.search(rm.no_rm)
        waktu_bst_search = time.time() - start_waktu

        # Format output angka desimal agar presisi (6 angka di belakang koma)
        print(f"{n:<5} | {waktu_enqueue:<15.6f} | {waktu_dequeue:<15.6f} | {waktu_bst_insert:<15.6f} | {waktu_bst_search:<15.6f}")
    
    print("=" * 75)
    print("Catatan: Salin tabel angka di atas untuk dimasukkan ke dalam laporan akhir.")

if __name__ == "__main__":
    jalankan_eksperimen()