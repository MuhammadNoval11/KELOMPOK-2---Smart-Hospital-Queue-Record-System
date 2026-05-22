import time, random
from modul_1 import PriorityQueue, Pasien
from modul_3 import BSTRekamMedis, RekorMedis

def jalankan_eksperimen():
    ukuran = [50, 200, 500]
    for n in ukuran:
        print(f"\n--- Eksperimen N = {n} ---")
        q = PriorityQueue("Poli Umum")
        bst = BSTRekamMedis()
        
        start = time.time()
        for i in range(n): q.enqueue(Pasien(i, "Pasien", "umum", 3))
        print(f"Enqueue: {(time.time()-start)*1000:.4f} ms")
        
        start = time.time()
        for i in range(n): bst.insert(RekorMedis(i, "Pasien"))
        print(f"BST Insert: {(time.time()-start)*1000:.4f} ms")

if __name__ == "__main__": jalankan_eksperimen()