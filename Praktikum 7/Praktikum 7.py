class DaftarNilaiMahasiswa:
    def __init__(self):
        self.data = {}
    def tambah(self, nama, nilai):
        self.data[nama] = nilai
        print(f"Data mahasiswa '{nama}' berhasil ditambahkan.")
    def tampilkan(self):
        if not self.data:
            print("Belum ada data mahasiswa.")
        else:
            print("\n=== Daftar Nilai Mahasiswa ===")
            for nama, nilai in self.data.items():
                print(f"Nama: {nama} | Nilai: {nilai}")
        print()
    def hapus(self, nama):
        if nama in self.data:
            del self.data[nama]
            print(f"Data mahasiswa '{nama}' berhasil dihapus.")
        else:
            print(f"Data '{nama}' tidak ditemukan.")
    def ubah(self, nama, nilai_baru):
        if nama in self.data:
            self.data[nama] = nilai_baru
            print(f"Data mahasiswa '{nama}' berhasil diubah.")
        else:
            print(f"Data '{nama}' tidak ditemukan.")
# ========== PROGRAM UTAMA ==========
mhs = DaftarNilaiMahasiswa()
while True:
    print("=== MENU ===")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Keluar")
    pilihan = input("Pilih menu (1-5): ")
    if pilihan == "1":
        nama = input("Masukkan nama: ")
        nilai = int(input("Masukkan nilai: "))
        mhs.tambah(nama, nilai)
    elif pilihan == "2":
        mhs.tampilkan()
    elif pilihan == "3":
        nama = input("Masukkan nama yang ingin diubah: ")
        nilai_baru = int(input("Masukkan nilai baru: "))
        mhs.ubah(nama, nilai_baru)
    elif pilihan == "4":
        nama = input("Masukkan nama yang ingin dihapus: ")
        mhs.hapus(nama)
    elif pilihan == "5":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")
