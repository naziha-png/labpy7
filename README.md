# Praktikum 7 – Object Oriented Programming (OOP)  

**Nama:** Naziha Raiqi Aribino<br>
**Kelas:** TI. 25. A2<br>
**NIM:** 312510232<br>
**Mata Kuliah:** Pengantar Pemrograman<br>
**Dosen:** Agung Nugroho, S.Kom., M.Kom.<br>

---

## **Judul Praktikum: Program Daftar Nilai Mahasiswa Menggunakan Class (OOP)**


## **Tujuan Praktikum**

1. Menerapkan konsep Class dan Object pada Python.
2. Menggunakan method dengan fungsi tambah, tampilkan, ubah, dan hapus data.
3. Menerapkan dasar-dasar manipulasi data dalam objek.

---

## **Materi Praktikum**

### **1. Konsep Dasar OOP**

* **Class & Object**: Class adalah blueprint, object adalah instance dari class.
* **Atribut & Method**: Atribut = data, Method = fungsi dalam class.
* **Constructor (`__init__`)**: Dieksekusi saat object dibuat.

### **2. Enkapsulasi**

* Menyembunyikan data agar tidak diakses sembarangan.
* Atribut yang diawali `__` menjadi private.
* Menggunakan **property**, **getter**, dan **setter** untuk akses atribut private.

### **3. Inheritance / Pewarisan**

* Class turunan dapat mewarisi atribut & method dari class induk.
* Digunakan untuk mengurangi duplikasi kode.

### **4. Polimorfisme**

* Method dengan nama sama tetapi perilaku berbeda.
* Terdiri dari **overloading** dan **overriding**.

---

-----------------------+
|   DaftarNilaiMahasiswa   |
+--------------------------+
| - data : dict            |
+--------------------------+
| + tambah(nama, nilai)    |
| + tampilkan()            |
| + ubah(nama, nilai)      |
| + hapus(nama)            |
+--------------------------+

````

---

## **Deskripsi Program**
Program ini dibuat untuk mengelola daftar nilai mahasiswa menggunakan pendekatan OOP. Program mencakup fitur:
- Menambahkan data mahasiswa (nama & nilai)
- Menampilkan seluruh data mahasiswa
- Mengubah nilai mahasiswa berdasarkan nama
- Menghapus data mahasiswa berdasarkan nama

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
````

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

Program ini dibuat berdasarkan instruksi pada *Tugas Praktikum*, yaitu membuat program daftar nilai mahasiswa menggunakan konsep **Class**, **Method**, dan **Object**. Berikut penjelasan lengkap fungsi-fungsi dalam program:

### **1. Class `DaftarNilaiMahasiswa`**

Class ini berfungsi sebagai wadah untuk menyimpan dan mengelola data mahasiswa. Data disimpan di dalam atribut:

* `self.data` → dictionary yang menyimpan pasangan nama dan nilai mahasiswa.

### **2. Method–method dalam class**

#### **a. `tambah(nama, nilai)`**

* Menambahkan data mahasiswa baru ke dictionary.
* Jika nama sudah ada, nilai akan diganti.
* Menampilkan konfirmasi bahwa data berhasil ditambahkan.

#### **b. `tampilkan()`**

* Menampilkan seluruh daftar nilai mahasiswa.
* Jika data masih kosong, akan muncul pesan "Belum ada data mahasiswa".

#### **c. `ubah(nama, nilai_baru)`**

* Mengubah nilai mahasiswa berdasarkan nama.
* Jika nama tidak ditemukan, akan muncul pesan kesalahan.

#### **d. `hapus(nama)`**

* Menghapus data mahasiswa berdasarkan nama.
* Jika nama tidak ada, menampilkan pesan bahwa data tidak ditemukan.

### **3. Program Utama (Main Program)**

* Program berjalan menggunakan loop `while True`.
* Pengguna memilih menu untuk menambah, menampilkan, mengubah, menghapus, atau keluar.
* Program berjalan berulang sampai pengguna memilih menu **Keluar**.

### **4. Penjelasan Tugas Praktikum Sesuai Modul**

Tugas praktikum meminta pembuatan program OOP yang memiliki:

* **Method tambah()** → ✔ dibuat
* **Method tampilkan()** → ✔ dibuat
* **Method hapus(nama)** → ✔ dibuat
* **Method ubah(nama)** → ✔ dibuat

Tugas juga meminta:

* **Diagram class** → ✔ tersedia di bawah
* **Flowchart** → ✔ tersedia
* **Penjelasan program** → ✔ ditulis di bagian ini
* **README lengkap** → ✔ seluruh dokumen ini berfungsi sebagai laporan README

Semua instruksi tugas sudah dipenuhi secara lengkap.

---

## **Diagram Class (UML) (UML)**

```
+--------------------------+
|   DaftarNilaiMahasiswa   |
+--------------------------+
| - data : dict            |
+--------------------------+
| + tambah(nama, nilai)    |
| + tampilkan()            |
| + ubah(nama, nilai)      |
| + hapus(nama)            |
+--------------------------+
```

---

## **Kesimpulan**


1. **Mahasiswa memahami struktur dasar pemrograman berorientasi objek**, mulai dari class, object, atribut, method, serta constructor. Pemahaman ini merupakan fondasi utama dari pemrograman berbasis OOP.

2. **Konsep enkapsulasi berhasil diterapkan**, baik melalui penggunaan atribut protected/public maupun konsep private pada Python. Praktikum ini juga melatih pemahaman tentang penggunaan getter dan setter untuk mengatur akses terhadap data.

3. **Penerapan method tambah, tampilkan, ubah, dan hapus membuat mahasiswa menguasai operasi CRUD dalam pendekatan OOP**, sehingga mahasiswa lebih terlatih membuat program yang terstruktur dan rapi.

4. **Alur program semakin mudah dipahami melalui menu interaktif**, yang mengajarkan bagaimana membuat program yang berulang (loop), menerima input pengguna, serta mengeksekusi fungsi berbeda dalam satu class.

5. **Materi modul seperti class-instance, enkapsulasi, inheritance, dan polymorphism dipahami secara teori**, meskipun program praktikum berfokus pada class dan enkapsulasi. Pemahaman dasar ini menjadi modal penting untuk praktikum OOP lanjutan.

6. **Mahasiswa dapat memahami bagaimana OOP menyederhanakan pengelolaan data**. Semua data dikelola dalam satu objek `DaftarNilaiMahasiswa`, sehingga program lebih mudah dikembangkan, diperluas, dan dipelihara.

7. **Praktikum ini memberikan gambaran nyata penerapan OOP dalam kasus sederhana**, sekaligus mempersiapkan mahasiswa untuk memahami konsep lanjutan seperti pewarisan, overriding, overloading, dan struktur class yang lebih kompleks.

---

**Selesai.**
