# Praktikum 7 – Object Oriented Programming (OOP)

**Nama:** Naziha Raiqi Aribino<br>
**Kelas:** TI.25.A2<br>
**NIM:** 312510232<br>
**Mata Kuliah:** Pengantar Pemrograman<br>
**Dosen Pengampu:** Agung Nugroho, S.Kom., M.Kom.<br>

---

## **Judul Praktikum**

**Program Daftar Nilai Mahasiswa Menggunakan Class (OOP)**


## **Tujuan Praktikum**

1. Menerapkan konsep Class dan Object pada Python.
2. Menggunakan method dengan fungsi tambah, tampilkan, ubah, dan hapus data.
3. Menerapkan dasar-dasar manipulasi data dalam objek.


## **Deskripsi Program**

Program ini dibuat untuk mengelola daftar nilai mahasiswa menggunakan pendekatan OOP. Program mencakup fitur:

* Menambahkan data mahasiswa (nama & nilai)
* Menampilkan seluruh data mahasiswa
* Mengubah nilai mahasiswa berdasarkan nama
* Menghapus data mahasiswa berdasarkan nama

Semua proses disimpan dalam satu class bernama `DaftarNilaiMahasiswa`.

---

## **Kode Program Lengkap**

```python
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
```

---

## **Flowchart Program**

```text
            ┌─────────────────────┐
            │     Mulai Program   │
            └──────────┬──────────┘
                       │
                       ▼
            ┌─────────────────────┐
            │   Tampilkan Menu    │
            └──────────┬──────────┘
                       │
                       ▼
            ┌─────────────────────┐
            │   Input Pilihan     │
            └──────────┬──────────┘
     ┌──────────────┬──┼───────────────┬───────────────┬───────────────┐
     ▼              ▼  ▼               ▼               ▼               ▼
┌──────────┐  ┌──────────┐      ┌──────────┐      ┌──────────┐   ┌──────────┐
│ Pilihan 1│  │ Pilihan 2│      │ Pilihan 3│      │ Pilihan 4│   │ Pilihan 5│
└────┬─────┘  └────┬─────┘      └────┬─────┘      └────┬─────┘   └────┬─────┘
     │             │                │                │            │
     ▼             ▼                ▼                ▼            ▼
┌──────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌──────────────────┐
│ Input    │ │ Tampilkan   │ │ Input Nama │ │ Input Nama │ │   Keluar Program │
│ Nama&Nilai│ │ Seluruh Data│ │ & Nilai Baru│ │ Hapus Data │ └──────────────────┘
└────┬─────┘ └──────┬─────┘ └──────┬─────┘ └──────┬─────┘
     │              │                │                │
     ▼              ▼                ▼                ▼
┌──────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐
│ Tambah   │ │ Selesai     │ │ Ubah Data  │ │ Hapus Data │
└────┬─────┘ └──────┬─────┘ └──────┬─────┘ └──────┬─────┘
     │              │                │                │
     └──────────────┴────────────────┴────────────────┴──────────→ kembali ke menu
```

---

## **Penjelasan Program**

Program ini menggunakan class untuk menyimpan data mahasiswa di dalam dictionary (`self.data`). Setiap method bekerja sebagai berikut:

* **tambah()** → menambahkan nama & nilai ke dalam dictionary.
* **tampilkan()** → menampilkan seluruh daftar data.
* **ubah()** → mengganti nilai mahasiswa berdasarkan nama.
* **hapus()** → menghapus data berdasarkan nama.

Program utama menggunakan loop `while True` untuk menampilkan menu hingga pengguna memilih keluar.

---

## **Kesimpulan**

Berikut adalah beberapa poin penting yang dapat disimpulkan dari praktikum ini:

1. **Pemahaman Konsep OOP**
   Praktikum ini membantu mahasiswa memahami konsep dasar OOP seperti *class*, *object*, atribut, dan method, serta bagaimana konsep tersebut digunakan dalam program nyata.

2. **Penerapan Method untuk Manipulasi Data**
   Mahasiswa belajar bagaimana membuat method untuk menambah, menampilkan, mengubah, dan menghapus data, sehingga terbiasa mengelola data secara terstruktur menggunakan OOP.

3. **Penggunaan Struktur Data dalam Class**
   Penggunaan dictionary di dalam class memberikan latihan dalam menggabungkan konsep OOP dan struktur data untuk menciptakan program yang lebih fleksibel dan efisien.

4. **Perancangan Alur Program dan Logika Menu**
   Dengan membuat menu interaktif, mahasiswa dilatih untuk berpikir logis dan menyusun alur program yang mudah digunakan oleh pengguna.

5. **Persiapan untuk Materi OOP yang Lebih Kompleks**
   Praktikum ini menjadi dasar penting sebelum mempelajari konsep OOP lanjutan seperti inheritance, polymorphism, dan encapsulation.

---

**Selesai.**
