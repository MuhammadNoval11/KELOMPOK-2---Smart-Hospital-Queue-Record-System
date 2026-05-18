import sys
import os

# Import BST dari data_structures
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'data_structures'))
from bst import BST, Node, DetailPenyakit


# ══════════════════════════════════════════════════
#  HELPER FUNCTIONS
# ══════════════════════════════════════════════════

def input_detail_penyakit():s
    print("\n  -- Detail Penyakit --")
    nama_penyakit = input("  Nama Penyakit     : ").strip().title()

    print("  Tingkat Keparahan :")
    print("    1. RINGAN")
    print("    2. SEDANG")
    print("    3. KRITIS")
    pilihan = input("  Pilih (1/2/3)     : ").strip()
    keparahan_map     = {"1": "RINGAN", "2": "SEDANG", "3": "KRITIS"}
    tingkat_keparahan = keparahan_map.get(pilihan, "RINGAN")

    gejala         = input("  Gejala           : ").strip().title()
    obat           = input("  Obat/Treatment   : ").strip().title()
    catatan_dokter = input("  Catatan Dokter   : ").strip().title()

    return DetailPenyakit(
        nama_penyakit,
        tingkat_keparahan,
        gejala,
        obat,
        catatan_dokter
    )


def tampil_detail(node):
    dp = node.detail_penyakit
    print("\nDATA PASIEN")
    print("-" * 40)
    print(f"No RM            : {node.no_rm}")
    print(f"Nama             : {node.nama}")
    print(f"Umur             : {node.umur} tahun")
    print("\nDETAIL PENYAKIT")
    print("-" * 40)
    print(f"Nama Penyakit    : {dp.nama_penyakit}")
    print(f"Tingkat Keparahan: {dp.tingkat_keparahan}")
    print(f"Gejala           : {dp.gejala}")
    print(f"Obat/Treatment   : {dp.obat}")
    print(f"Catatan Dokter   : {dp.catatan_dokter}")
    print("-" * 40)


# ══════════════════════════════════════════════════
#  MENU FUNCTIONS
# ══════════════════════════════════════════════════

def menu_tambah(bst):
    print("\nTAMBAH REKAM MEDIS")
    print("-" * 25)
    no_rm_input = input("Nomor RM    : ").strip()
    no_rm       = "RM" + no_rm_input
    nama        = input("Nama Pasien : ").strip().title()
    umur        = input("Umur        : ").strip()

    if not no_rm_input or not nama or not umur:
        print("\nSemua field harus diisi!")
        return

    detail   = input_detail_penyakit()
    berhasil = bst.insert(no_rm, nama, umur, detail)

    if berhasil:
        print(f"\nData {nama} berhasil ditambahkan! (No RM: {no_rm})")
    else:
        print(f"\nNo RM {no_rm} sudah ada!")


def menu_cari(bst):
    print("\nCARI REKAM MEDIS")
    print("-" * 25)
    no_rm_input = input("Nomor RM : ").strip()
    no_rm       = "RM" + no_rm_input

    hasil = bst.search(no_rm)
    if hasil:
        tampil_detail(hasil)
    else:
        print(f"\nNo RM {no_rm} tidak ditemukan!")


def menu_hapus(bst):
    print("\nHAPUS REKAM MEDIS")
    print("-" * 25)
    no_rm_input = input("Nomor RM : ").strip()
    no_rm       = "RM" + no_rm_input

    hasil = bst.search(no_rm)
    if hasil is None:
        print(f"\nNo RM {no_rm} tidak ditemukan!")
        return

    tampil_detail(hasil)
    konfirmasi = input(f"\nHapus data {hasil.nama}? (y/n) : ")
    if konfirmasi.lower() == 'y':
        bst.delete(no_rm)
        print(f"\nData {hasil.nama} berhasil dihapus!")
    else:
        print("\nPenghapusan dibatalkan!")


def menu_detail(bst):
    print("\nLIHAT DETAIL PENYAKIT")
    print("-" * 25)
    no_rm_input = input("Nomor RM : ").strip()
    no_rm       = "RM" + no_rm_input

    hasil = bst.search(no_rm)
    if hasil:
        tampil_detail(hasil)
    else:
        print(f"\nNo RM {no_rm} tidak ditemukan!")


def menu_tampil_semua(bst):
    print("\nSEMUA DATA REKAM MEDIS")
    print("-" * 25)
    bst.tampil_semua()


def tampil_menu():
    print("\nSISTEM REKAM MEDIS - BST")
    print("-" * 25)
    print("1. Tambah Data Pasien")
    print("2. Cari Data Pasien")
    print("3. Hapus Data Pasien")
    print("4. Tampil Semua Data")
    print("5. Lihat Detail Penyakit")
    print("0. Keluar")
    print("-" * 25)


# ══════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════

def main():
    bst = BST()

    # Data awal untuk testing
    bst.insert("RM001", "Budi Santoso", "32",
        DetailPenyakit(
            "Demam Berdarah", "SEDANG",
            "Demam Tinggi, Bintik Merah",
            "Parasetamol, Infus",
            "Pantau trombosit setiap 6 jam"
        )
    )
    bst.insert("RM002", "Siti Aminah", "25",
        DetailPenyakit(
            "Hipertensi", "KRITIS",
            "Pusing, Tekanan Darah 180/110",
            "Amlodipine 10mg",
            "Bed rest, hindari garam"
        )
    )
    bst.insert("RM003", "Ahmad Fauzi", "40",
        DetailPenyakit(
            "Flu Biasa", "RINGAN",
            "Pilek, Batuk Ringan",
            "Vitamin C, Paracetamol",
            "Istirahat cukup, banyak minum air"
        )
    )

    while True:
        tampil_menu()
        pilihan = input("Pilih menu (0-5) : ").strip()

        if pilihan == "1":
            menu_tambah(bst)
        elif pilihan == "2":
            menu_cari(bst)
        elif pilihan == "3":
            menu_hapus(bst)
        elif pilihan == "4":
            menu_tampil_semua(bst)
        elif pilihan == "5":
            menu_detail(bst)
        elif pilihan == "0":
            print("\nTerima kasih, sampai jumpa!\n")
            break
        else:
            print("\nPilihan tidak valid, coba lagi!")


if __name__ == "__main__":
    main()