"""
====================================================================
PROJECT    : Implementasi Algoritma Dijkstra untuk Peta Kota
MATAKULIAH : Struktur Data
DOSEN      : Ibu Kartini
MAHASISWA  : Farrel Gian, Francesko Efhraim, Muhammad Fauzan, Deva Bagus Pramodya
UNIVERSITAS: Universitas Esa Unggul
====================================================================

DESKRIPSI:
Program ini mengimplementasikan algoritma Dijkstra untuk mencari 
jalur terpendek pada graf peta kota. Menggunakan struktur data 
Binary Heap (Priority Queue) buatan sendiri untuk efisiensi, 
bukan menggunakan library bawaan.

ANALISIS KOMPLEKSITAS (BIG O):
- Time Complexity : O((V + E) log V)
    * V = Jumlah Vertex (Lokasi/Simpul)
    * E = Jumlah Edge (Jalan/Sisi)
    * log V = Biaya operasi pada Binary Heap (push/pop)
- Space Complexity: O(V + E)
    * Menggunakan Adjacency List untuk menyimpan graf agar efisien 
      dalam memori dibandingkan Adjacency Matrix.

STRUKTUR DATA YANG DIGUNAKAN:
- Binary Heap (Min-Heap) : Sebagai Priority Queue manual untuk 
  mempercepat pencarian node dengan jarak minimum.
- Dictionary (Hash Map)  : Sebagai Adjacency List untuk representasi 
  peta kota.
====================================================================
"""

import os
import json
from collections import defaultdict
from logic import dijkstra
import networkx as nx
import matplotlib.pyplot as plt

# State global untuk menyimpan peta
city_map = defaultdict(dict)

def clear_screen():
    """Bersihkan layar terminal agar tampilan menu lebih rapi."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header():
    """Tampilkan header program pada layar."""
    header = r"""
  ____   _  _____ _   _     _____ ___ _   _ ____  _____ ____  
 |  _ \ / \|_   _| | | |   |  ___|_ _| \ | |  _ \| ____|  _ \ 
 | |_) / _ \ | | | |_| |   | |_   | ||  \| | | | |  _| | |_) |
 |  __/ ___ \| | |  _  |   |  _|  | || |\  | |_| | |___|  _ < 
 |_| /_/   \_\_| |_| |_|   |_|   |___|_| \_|____/|_____|_| \_\
    """
    print(header)
    print("           [ Algoritma Dijkstra - Peta Kota ]")
    print("=" * 60)


def simpan_peta():
    """Simpan data peta ke file JSON agar dapat dipakai lagi nanti."""
    nama_file = "peta_data.json"
    try:
        with open(nama_file, 'w') as f:
            json.dump(dict(city_map), f, indent=4)
        print(f"\n[+] Peta berhasil disimpan ke {nama_file}")
    except Exception as e:
        print(f"\n[!] Gagal menyimpan: {e}")
    input("\nTekan Enter untuk kembali...")


def muat_peta():
    """Muat data peta dari file JSON ke memori program."""
    global city_map
    nama_file = "peta_data.json"
    if not os.path.exists(nama_file):
        print("\n[!] File tidak ditemukan!")
    else:
        try:
            with open(nama_file, 'r') as f:
                data = json.load(f)
                city_map = defaultdict(dict, data)
            print("\n[+] Peta berhasil dimuat!")
        except Exception as e:
            print(f"\n[!] Gagal memuat: {e}")
    input("\nTekan Enter untuk kembali...")


def tambah_titik():
    """Tambah titik dan hubungan jalan baru ke dalam peta."""
    print("\n--- TAMBAH TITIK/HUBUNGAN ---")
    asal = input("Lokasi Asal  : ").strip()
    tujuan = input("Lokasi Tujuan: ").strip()
    try:
        jarak = float(input("Jarak (km)   : "))
        city_map[asal][tujuan] = jarak
        city_map[tujuan][asal] = jarak
        print(f"\n[+] Berhasil menambah jalur {asal} <-> {tujuan}")
    except ValueError:
        print("[!] Input jarak harus angka!")
    input("\nTekan Enter untuk kembali...")


def visualisasi_peta():
    """Tampilkan seluruh hubungan antar titik yang ada pada peta."""
    print("\n--- VISUALISASI HUBUNGAN ANTAR TITIK ---")
    if not city_map:
        print("Peta masih kosong!")
    else:
        for node, neighbors in city_map.items():
            koneksi = ", ".join([f"{n}({w}km)" for n, w in neighbors.items()])
            print(f"{node} terhubung ke: {koneksi}")
    input("\nTekan Enter untuk kembali...")


def visualisasi_grafis():
    if not city_map:
        print("\n[!] Peta masih kosong!")
        return

    # Membuat objek graph dari data manual kita
    G = nx.Graph()
    for node, neighbors in city_map.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)

    # Pengaturan posisi node agar rapi
    pos = nx.spring_layout(G)
    
    # Menggambar node dan garis
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=10)
    
    # Menambahkan label bobot (jarak) di atas garis
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    
    plt.title("Visualisasi Topologi Peta Kota")
    plt.show()

def rute_terbaik():
    """Minta input titik awal dan tujuan lalu tampilkan rute terpendek."""
    print("\n--- TENTUKAN RUTE TERBAIK ---")
    start = input("Titik Awal  : ").strip()
    end = input("Titik Tujuan: ").strip()

    if start not in city_map or end not in city_map:
        print("[!] Lokasi tidak ditemukan!")
    else:
        path, distance = dijkstra(city_map, start, end)
        if path:
            print(f"\nRute: {' -> '.join(path)}")
            print(f"Total Jarak: {distance} km")
        else:
            print("[!] Rute tidak ditemukan karna lokasi tidak terhubung!")
    input("\nTekan Enter untuk kembali...")



def main():
    """Jalankan menu interaktif utama program."""
    while True:
        clear_screen()
        print_header()
        print("Menu Utama:")
        print("1. Tambah Titik")
        print("2. Visualisasi Teks")
        print("3. Visualisasi Grafis (Peta)") # Menu Baru
        print("4. Tentukan Rute Terbaik")
        print("5. Simpan Peta")
        print("6. Muat Peta")
        print("7. Keluar")

        pilihan = input("\nPilih menu (1-7): ")

        if pilihan == '1':
            tambah_titik()
        elif pilihan == '2':
            visualisasi_peta()
        elif pilihan == '3':
            visualisasi_grafis()
        elif pilihan == '4':
            rute_terbaik()
        elif pilihan == '5':
            simpan_peta()
        elif pilihan == '6':
            muat_peta()
        elif pilihan == '7':    
            print("\nTerima kasih!")
            break


if __name__ == "__main__":
    main()