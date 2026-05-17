BANNER = r"""
╔══════════════════════════════════════════════════════════╗
║     SISTEM ANTRIAN RUMAH SAKIT — CLI INTERAKTIF          ║
║     Struktur Data: Priority Queue + BST + Stack          ║
╚══════════════════════════════════════════════════════════╝
"""

HELP_TEXT = """
┌─────────────────────────────────────────────────────────────┐
│  PERINTAH TERSEDIA                          Big-O           │
├─────────────────────────────────────────────────────────────┤
│  DAFTAR <nama> <poli> <prioritas>           O(n) enqueue    │
│  PANGGIL <poli> [id_dokter]                 O(1) dequeue    │
│  UNDO_DOKTER <id_dokter>                    O(1) pop        │
│  CARI_RM <no_rm>                            O(log n) search │
│  TAMBAH_RM <no_rm:nama:poli:prioritas>      O(log n) insert │
│  LAPORAN_HARI [insertion|selection]         O(n²) sort      │
│  STATUS                                     O(1)            │
│  EKSPERIMEN                                 Jalankan Modul 6│
│  BANTUAN                                    Tampilkan ini   │
│  KELUAR                                     Keluar sistem   │
├─────────────────────────────────────────────────────────────┤
│  Poli: Umum | Anak | Jantung | Ortopedi | Saraf             │
│  Prioritas: NORMAL | TINGGI | KRITIS                        │
└─────────────────────────────────────────────────────────────┘
"""

def jalankan_cli():
  print(BANNER)
  print(HELP_TEXT)

sistem = SistemRumahSakit()

# Seed Data Awal
data_awal = [
  ("Budi Santoso", "Umum", "NORMAL"),
  ("Siti Rahayu", "Jantung", "KRITIS"),
  ("Ahmad Fauzi", "Anak", "TINGGI"),
  ("Dewi Lestari", "Umum", "NORMAL"),
  ("Rudi Hartono", "Jantung", "TINGGI"),
]
print("  [Seed Data] Mendaftarkan pasien awal...\n")
for nama, poli, prio in data_awal:
  ok, msg = sistem.daftar(nama, poli, prio)
  if ok:
    print(f"  + {nama} → {poli} ({prio})")
print()

while True:
  try:
    raw = input("  ▶ ").strip()
  except (EOFError, KeyboardInterrupt):
    print("\n  Keluar dari sistem. Sampai jumpa!")
    break

if not raw:
  continue

parts = raw.split()
cmd = parts[0].upper()

if cmd == "KELUAR":
  print("  👋 Sistem ditutup. Terima kasih!")
  break

elif cmd == "BANTUAN":
  print(HELP_TEXT)

elif cmd == "STATUS":
  print(sistem.status_antrian())

elif cmd == "DAFTAR":
  if len(parts) < 4:
    print("  ❌ Penggunaan: DAFTAR <nama> <poli> <prioritas>")
  else:
    nama = parts[1]
    poli = parts[2]
    prioritas = parts[3]
    ok, msg = sistem.daftar(nama, poli, prioritas)
    print(f"\n{msg}\n")

elif cmd == "UNDO_DOKTER":
  if len(parts) < 2:
    print("  ❌ Penggunaan: UNDO_DOKTER <id_dokter>")
  else:
    ok, msg = sistem.undo_dokter(parts[1])
    print(f"\n{msg}\n")

elif cmd == "CARI_RM":
  if len(parts) < 2:
    print("  ❌ Penggunaan: CARI_RM <no_rm>")
  else:
    ok, msg = sistem.cari_rm(parts[1])
    print(f"\n{msg}\n")

elif cmd == "TAMBAH_RM":
  if len(parts) < 2:
    print("  ❌ Penggunaan: TAMBAH_RM <no_rm:nama:poli:prioritas>")
  else:
    ok, msg = sistem.tambah_rm(parts[1])
    print(f"\n{msg}\n")

elif cmd == "LAPORAN_HARI":
  metode = parts[1] if len(parts) > 1 else "insertion"
  key = parts[2] if len(parts) > 2 else "waktu_tunggu"
  ok, msg = sistem.laporan_hari(metode, key)
  print(f"\n{msg}\n")

elif cmd == "EKSPERIMEN":
  jalankan_eksperimen()
  
else:
  print(f"  ❓ Perintah '{cmd}' tidak dikenal. Ketik BANTUAN untuk daftar perintah.")

print()


if __name__ = "__main__":
import sys
if len(sys.argv) > 1 and sys.argv[1] == "--eksperimen":
  jalankan_eksperimen()
else:
  jalankan_cli()
