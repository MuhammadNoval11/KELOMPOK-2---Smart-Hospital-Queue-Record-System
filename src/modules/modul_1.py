<<<<<<< HEAD
from typing import Optional

class Pasien:
    def __init__(self, nama: str, prioritas: int):
        self.data = f"{nama} (Prioritas: {prioritas})"
        self.prioritas = prioritas
        self.next = None

class PriorityQueue:
    def __init__(self, nama_poli: str):
        self.poli = nama_poli
        self.head: Optional[Pasien] = None
        self.size: int = 0
        
    def is_empty(self) -> bool:
        return self.head is None

    def enqueue(self, nama: str, prioritas: int):
        pasien_baru = Pasien(nama, prioritas)
        if self.is_empty():
            self.head = pasien_baru
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = pasien_baru
        self.size += 1

    def dequeue(self) -> Optional[str]:
        if self.is_empty():
            return None
        
        pasien = self.head.data
        self.head = self.head.next
        self.size -= 1
        return pasien

    def peek(self) -> Optional[str]:
        if self.is_empty():
            return None
        return self.head.data

    def tampilkan(self):
        if self.is_empty():
            print(f"[{self.poli}] Antrian kosong.")
            return
        
        print(f"\n--- Daftar Antrean [{self.poli}] ---")
        current = self.head
        urutan = 1
        while current:
            print(f"{urutan}. {current.data}")
            current = current.next
            urutan += 1
        print("------------------------------")


if __name__ == "__main__":
    # Bikin objek antrean
    antrean_ugd = PriorityQueue("Poli UGD")
    
    # Cek antrean pas masih kosong
    antrean_ugd.tampilkan()
    
    # Masukin data dummy buat ngetes
    antrean_ugd.enqueue("Budi", 1)
    antrean_ugd.enqueue("Siti", 2)
    antrean_ugd.enqueue("Andi", 1)
    # Liat isi antrean
    antrean_ugd.tampilkan()
    
    # Ngetes fungsi peek sama dequeue punya kamu
    print(f"Pasien terdepan: {antrean_ugd.peek()}")
    
    dipanggil = antrean_ugd.dequeue()
    print(f"PANGGILAN: Pasien {dipanggil} silakan masuk.")
    
    # Liat sisa antrean
    antrean_ugd.tampilkan()
=======
>>>>>>> feat/Belva-EksperimenValidasi
