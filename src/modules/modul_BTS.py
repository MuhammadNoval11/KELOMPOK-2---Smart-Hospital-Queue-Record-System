class Node:
    def __init__(self, no_rm, nama, penyakit, umur):
        self.no_rm    = no_rm
        self.nama     = nama
        self.penyakit = penyakit
        self.umur     = umur
        self.left     = None
        self.right    = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, no_rm, nama, penyakit, umur):
        node_baru = Node(no_rm, nama, penyakit, umur)
        if self.root is None:
            self.root = node_baru
            return True
        current = self.root
        while True:
            if no_rm < current.no_rm:
                if current.left is None:
                    current.left = node_baru
                    return True
                current = current.left
            elif no_rm > current.no_rm:
                if current.right is None:
                    current.right = node_baru
                    return True
                current = current.right
            else:
                return False

    def search(self, no_rm):
        current = self.root
        while current:
            if no_rm == current.no_rm:
                return current
            elif no_rm < current.no_rm:
                current = current.left
            else:
                current = current.right
        return None

    def delete(self, no_rm):
        self.root, berhasil = self._delete(self.root, no_rm)
        return berhasil

    def _delete(self, node, no_rm):
        if node is None:
            return None, False
        if no_rm < node.no_rm:
            node.left, berhasil = self._delete(node.left, no_rm)
        elif no_rm > node.no_rm:
            node.right, berhasil = self._delete(node.right, no_rm)
        else:
            berhasil = True
            if node.left is None and node.right is None:
                return None, berhasil
            elif node.left is None:
                return node.right, berhasil
            elif node.right is None:
                return node.left, berhasil
            else:
                successor      = self._min_node(node.right)
                node.no_rm    = successor.no_rm
                node.nama     = successor.nama
                node.penyakit = successor.penyakit
                node.umur     = successor.umur
                node.right, _ = self._delete(node.right, successor.no_rm)
        return node, berhasil

    def _min_node(self, node):
        while node.left:
            node = node.left
        return node

    def inorder(self):
        hasil = []
        self._inorder(self.root, hasil)
        return hasil

    def _inorder(self, node, hasil):
        if node:
            self._inorder(node.left, hasil)
            hasil.append(node)
            self._inorder(node.right, hasil)

    def tampil_semua(self):
        data = self.inorder()
        if not data:
            print("\nBST kosong, belum ada data!")
            return
        print(f"\n{'No RM':<10} {'Nama':<22} {'Umur':<6} {'Penyakit'}")
        print("-" * 50)
        for n in data:
            print(f"{n.no_rm:<10} {n.nama:<22} {n.umur:<6} {n.penyakit}")
        print(f"\nTotal data: {len(data)} pasien")


def menu_tambah(bst):
    print("\nTAMBAH REKAM MEDIS")
    print("-" * 25)
    no_rm_input = input("Nomor RM    : ").strip()
    no_rm = "RM" + no_rm_input
    nama = input("Nama Pasien : ").strip().title()
    umur = input("Umur        : ").strip()
    penyakit = input("Penyakit    : ").strip().title()

    if not no_rm or not nama or not umur or not penyakit:
        print("\nSemua field harus diisi!")
        return

    berhasil = bst.insert(no_rm, nama, penyakit, umur)
    if berhasil:
        print(f"\nData {nama} berhasil ditambahkan dengan No RM {no_rm}!")
    else:
        print(f"\nNo RM {no_rm} sudah ada!")


def menu_cari(bst):
    print("\nCARI REKAM MEDIS")
    print("-" * 25)
    no_rm_input = input("Masukkan No RM : ").strip()
    no_rm = "RM" + no_rm_input

    hasil = bst.search(no_rm)
    if hasil:
        print("\nData Ditemukan!")
        print("-" * 30)
        print(f"No RM    : {hasil.no_rm}")
        print(f"Nama     : {hasil.nama}")
        print(f"Umur     : {hasil.umur} tahun")
        print(f"Penyakit : {hasil.penyakit}")
        print("-" * 30)
    else:
        print(f"\nNo RM {no_rm} tidak ditemukan!")


def menu_hapus(bst):
    print("\nHAPUS REKAM MEDIS")
    print("-" * 25)
    no_rm_input = input("Masukkan No RM : ").strip()
    no_rm = "RM" + no_rm_input


    hasil = bst.search(no_rm)
    if hasil is None:
        print(f"\nNo RM {no_rm} tidak ditemukan!")
        return

    konfirmasi = input(f"Hapus data {hasil.nama}? (y/n) : ")
    if konfirmasi.lower() == 'y':
        bst.delete(no_rm)
        print(f"\nData {hasil.nama} berhasil dihapus!")
    else:
        print("\nPenghapusan dibatalkan!")


def tampil_menu():
    print("\nSISTEM REKAM MEDIS - BST")
    print("-" * 25)
    print("1. Tambah Data Pasien")
    print("2. Cari Data Pasien")
    print("3. Hapus Data Pasien")
    print("4. Tampil Semua Data")
    print("0. Keluar")
    print("-" * 25)


if __name__ == "__main__":
    bst = BST()

    bst.insert("RM001", "Black Cats", "Flu", "05")

    while True:
        tampil_menu()
        pilihan = input("Pilih menu (input nomor) : ").strip()

        if pilihan == "1":
            menu_tambah(bst)
        elif pilihan == "2":
            menu_cari(bst)
        elif pilihan == "3":
            menu_hapus(bst)
        elif pilihan == "4":
            print("\nSEMUA DATA REKAM MEDIS")
            print("-" * 25)
            bst.tampil_semua()
        elif pilihan == "0":
            print("\nTerima kasih, sampai jumpa!\n")
            break
        else:
            print("\nPilihan tidak valid, coba lagi!")