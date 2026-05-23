from dataclasses import dataclass, field
from typing import Optional, List

# 1. Struktur Data Rekam Medis (Sesuai panduan PDF)
@dataclass
class RekorMedis:
    no_rm: int
    nama: str
    riwayat: List[str] = field(default_factory=list)

# 2. Node untuk BST
class BSTNode:
    def __init__(self, rekord: RekorMedis):
        self.rekord = rekord
        self.left: Optional['BSTNode'] = None
        self.right: Optional['BSTNode'] = None

# 3. Class BST Utama
class BSTRekamMedis:
    def __init__(self):
        self.root: Optional[BSTNode] = None

    def insert(self, rekord: RekorMedis) -> None:
        """Memasukkan data RM baru. Big-O: rata-rata O(log n)."""
        if self.root is None:
            self.root = BSTNode(rekord)
            return
        
        # Logika iteratif biar lebih aman dari error batas rekursi
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
                # Kalau no_rm sudah ada, abaikan (mencegah duplikat)
                break

    def search(self, no_rm: int) -> Optional[RekorMedis]:
        """Mencari data berdasarkan nomor RM. Big-O: rata-rata O(log n)."""
        curr = self.root
        while curr:
            if no_rm == curr.rekord.no_rm:
                return curr.rekord
            elif no_rm < curr.rekord.no_rm:
                curr = curr.left
            else:
                curr = curr.right
        return None # Return None kalau tidak ketemu

    def inorder(self) -> List[RekorMedis]:
        """Menampilkan semua RM terurut dari no terkecil. Big-O: O(n)."""
        hasil = []
        def _inorder(node: Optional[BSTNode]):
            if node:
                _inorder(node.left)
                hasil.append(node.rekord)
                _inorder(node.right)
        
        _inorder(self.root)
        return hasil

# ==========================================
# Blok Eksekusi (Uji Coba Standalone)
# ==========================================
if __name__ == "__main__":
    bst = BSTRekamMedis()

    # 1. Menambahkan beberapa data pasien acak
    pasien1 = RekorMedis(105, "Andi", ["Demam", "Flu"])
    pasien2 = RekorMedis(102, "Budi", ["Pusing"])
    pasien3 = RekorMedis(108, "Citra", ["Asam Lambung"])
    pasien4 = RekorMedis(101, "Dewi", ["Cek Darah"])

    for p in [pasien1, pasien2, pasien3, pasien4]:
        bst.insert(p)
        print(f"  [INSERT] Berhasil memasukkan RM {p.no_rm} ({p.nama})")

    # 2. Menguji pencarian data
    print("\n=== Menguji Fitur Pencarian ===")
    target = 108
    hasil_cari = bst.search(target)
    if hasil_cari:
        print(f"  Ditemukan: Pasien {hasil_cari.nama} (RM {hasil_cari.no_rm}), Riwayat: {hasil_cari.riwayat}")
    else:
        print(f"  Pasien dengan RM {target} tidak ditemukan.")

    # 3. Menampilkan semua data secara terurut (Inorder Traversal)
    print("\n=== Daftar Semua Rekam Medis (Terurut) ===")
    semua_data = bst.inorder()
    for data in semua_data:
        print(f"  RM {data.no_rm} - {data.nama}")