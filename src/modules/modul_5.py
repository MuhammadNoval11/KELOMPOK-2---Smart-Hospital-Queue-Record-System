# File: src/modules/modul_5.py
from modul_1 import PriorityQueue, Pasien, PRIORITAS_MAP, POLI
from modul_2 import Stack
from modul_3 import BSTRekamMedis, RekorMedis
from modul_4 import LaporanSelesai

def main():
    # Inisialisasi struktur data sistem antrean
    queues = {p: PriorityQueue(p) for p in POLI}
    dokter_stacks = {p: Stack(f"Dokter {p.capitalize()}") for p in POLI}
    bst_rm = BSTRekamMedis()
    laporan = LaporanSelesai()
    
    counter_antrian = 1
    
    print("="*50)
    print(" SMART HOSPITAL QUEUE & RECORD SYSTEM ")
    print(" Ketik BANTUAN untuk melihat daftar perintah ")
    print("="*50)

    while True:
        try:
            cmd_raw = input("\n>> ").strip().split()
            if not cmd_raw: continue
            cmd = cmd_raw[0].upper()
            
            if cmd == "BANTUAN":
                print("Perintah: DAFTAR, PANGGIL, UNDO_DOKTER, CARI_RM, TAMBAH_RM, LAPORAN_HARI, KELUAR")

            elif cmd == "DAFTAR" and len(cmd_raw) >= 4:
                nama, poli, pri_str = cmd_raw[1], cmd_raw[2].lower(), cmd_raw[3].upper()
                if poli in POLI and pri_str in PRIORITAS_MAP:
                    pasien_baru = Pasien(counter_antrian, nama, poli, PRIORITAS_MAP[pri_str])
                    queues[poli].enqueue(pasien_baru)
                    print(f"  -> [Big-O: O(n)] {nama} masuk antrean {poli}.")
                    counter_antrian += 1
                else:
                    print("  Poli atau Prioritas tidak valid.")

            elif cmd == "PANGGIL" and len(cmd_raw) >= 2:
                poli = cmd_raw[1].lower()
                if poli in queues:
                    pasien = queues[poli].dequeue()
                    if pasien:
                        laporan.tambah_selesai(pasien)
                        dokter_stacks[poli].push(f"Memeriksa {pasien.nama}")
                        print(f"  -> [Big-O: O(1)] {pasien.nama} dipanggil ke {poli}.")
                    else:
                        print(f"  Antrean {poli} kosong.")

            elif cmd == "UNDO_DOKTER" and len(cmd_raw) >= 2:
                poli = cmd_raw[1].lower()
                if poli in dokter_stacks:
                    batal = dokter_stacks[poli].pop()
                    print(f"  -> [Big-O: O(1)] Batal: {batal}" if batal else "  Tidak ada histori.")

            elif cmd == "CARI_RM" and len(cmd_raw) >= 2:
                hasil = bst_rm.search(int(cmd_raw[1]))
                if hasil:
                    print(f"  -> [Big-O: O(log n)] Ditemukan: {hasil.nama}")
                else:
                    print("  -> RM tidak ditemukan.")

            elif cmd == "TAMBAH_RM" and len(cmd_raw) >= 3:
                no_rm, nama = int(cmd_raw[1]), cmd_raw[2]
                bst_rm.insert(RekorMedis(no_rm, nama))
                print(f"  -> [Big-O: O(log n)] RM {no_rm} ditambahkan.")

            elif cmd == "LAPORAN_HARI":
                print("  -> [Big-O: O(n^2)] Mengurutkan laporan...")
                laporan.sort_berdasarkan_no_antrian()
                print("\n=== PASIEN SELESAI ===")
                laporan.tampilkan()

            elif cmd == "KELUAR":
                break
        except Exception as e:
            print(f"  Error: {e}")

if __name__ == "__main__":
    main()