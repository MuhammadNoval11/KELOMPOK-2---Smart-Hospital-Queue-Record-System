class DetailPenyakit:
    def __init__(self, nama_penyakit, tingkat_keparahan, gejala, obat, catatan_dokter):
        self.nama_penyakit     = nama_penyakit
        self.tingkat_keparahan = tingkat_keparahan
        self.gejala            = gejala
        self.obat              = obat
        self.catatan_dokter    = catatan_dokter


class Node:
    def __init__(self, no_rm, nama, umur, detail_penyakit):
        self.no_rm           = no_rm
        self.nama            = nama
        self.umur            = umur
        self.detail_penyakit = detail_penyakit
        self.left            = None
        self.right           = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, no_rm, nama, umur, detail_penyakit):
        node_baru = Node(no_rm, nama, umur, detail_penyakit)
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
            node.left, berhasil  = self._delete(node.left, no_rm)
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
                successor            = self._min_node(node.right)
                node.no_rm           = successor.no_rm
                node.nama            = successor.nama
                node.umur            = successor.umur
                node.detail_penyakit = successor.detail_penyakit
                node.right, _        = self._delete(node.right, successor.no_rm)
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
        print(f"\n{'No RM':<10} {'Nama':<22} {'Umur':<6} {'Penyakit':<20} {'Keparahan'}")
        print("-" * 65)
        for n in data:
            dp = n.detail_penyakit
            print(f"{n.no_rm:<10} {n.nama:<22} {n.umur:<6} {dp.nama_penyakit:<20} {dp.tingkat_keparahan}")
        print(f"\nTotal: {len(data)} pasien")