# Path Finder

Program ini merupakan tugas akhir mata kuliah Struktur Data yang mengimplementasikan algoritma Dijkstra untuk mencari jalur terpendek pada peta kota. Aplikasi ini dibuat sebagai contoh nyata penerapan konsep graf dan struktur data dalam pemrograman.

## Deskripsi Program

Path Finder adalah aplikasi interaktif berbasis terminal yang memungkinkan pengguna untuk:
- menambah titik lokasi dan hubungan antar lokasi,
- melihat representasi peta secara teks,
- melihat visualisasi graf secara grafis,
- mencari rute terpendek dari satu titik ke titik lain,
- menyimpan dan memuat data peta ke file JSON.

Program ini sangat cocok untuk memahami bagaimana algoritma pencarian jalur bekerja pada data berbentuk graf.

## Implementasi Materi Struktur Data

Program ini menerapkan beberapa konsep penting dalam mata kuliah Struktur Data, antara lain:

1. Graph (Graf)
   - Peta kota direpresentasikan sebagai graf.
   - Setiap lokasi dianggap sebagai simpul (node), sedangkan jalan antar lokasi dianggap sebagai sisi (edge).
   - Setiap sisi memiliki bobot berupa jarak dalam kilometer.

2. Adjacency List
   - Data graf disimpan menggunakan struktur dictionary yang berisi hubungan antar node.
   - Struktur ini efisien untuk merepresentasikan graf yang sparse.

3. Priority Queue / Binary Heap
   - Algoritma Dijkstra menggunakan antrian prioritas untuk memilih node dengan jarak terkecil berikutnya.
   - Implementasi priority queue dibuat manual tanpa memanfaatkan library bawaan.

4. Path Finding
   - Program mencari jalur terpendek dengan algoritma Dijkstra.
   - Hasil yang ditampilkan berupa rute dan total jarak.

## Fitur Utama

- Tambah titik dan hubungan jalan baru
- Visualisasi hubungan antar titik dalam bentuk teks
- Visualisasi graf secara grafis
- Mencari rute terpendek dengan Dijkstra
- Menyimpan dan memuat data peta ke file JSON

## Persyaratan

Pastikan Python sudah terinstal di sistem Anda.

Instal dependensi yang diperlukan:

```bash
pip install networkx matplotlib
```

## Cara Menjalankan Program

1. Buka terminal di folder proyek.
2. Jalankan perintah berikut:

```bash
python main.py
```

3. Pilih menu yang tersedia:
   - 1: Tambah Titik
   - 2: Visualisasi Teks
   - 3: Visualisasi Grafis
   - 4: Tentukan Rute Terbaik
   - 5: Simpan Peta
   - 6: Muat Peta
   - 7: Keluar

## Catatan

Program ini dibuat untuk keperluan pembelajaran dan demonstrasi penerapan algoritma Dijkstra serta struktur data graf dalam pemecahan masalah nyata.
