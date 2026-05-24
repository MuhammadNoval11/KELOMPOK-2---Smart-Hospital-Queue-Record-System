class GraphRujukan:
    def __init__(self):
        # Menyimpan daftar unit dan tetangga rujukan yang terhubung
        self.adj_list = {}

    # Tahap 1: Menambahkan unit poli/ruangan ke dalam peta
    def tambah_unit(self, nama_unit):
        if nama_unit not in self.adj_list:
            self.adj_list[nama_unit] = []

    # Tahap 2: Membuat jalur rujukan antar unit (Directed Graph / Satu Arah)
    def tambah_rujukan(self, asal, tujuan):
        # Pastikan kedua unit sudah terdaftar
        if asal in self.adj_list and tujuan in self.adj_list:
            self.adj_list[asal].append(tujuan)
            
    # Tahap 3: Melihat unit mana saja yang bisa dirujuk dari unit tertentu
    def lihat_jalur_rujukan(self, asal):
        if asal in self.adj_list:
            return self.adj_list[asal]
        return []
    