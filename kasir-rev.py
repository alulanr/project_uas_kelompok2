from prettytable import PrettyTable
from datetime import datetime

def tampilkan_tabel_menu(tabel_menu, daftar_menu, judul):
    for i, (menu, harga) in enumerate(daftar_menu, start=1):
        tabel_menu.add_row([i, menu, harga])

    print(f"{judul}:")
    print(tabel_menu)

def hitung_total_pesanan(pesanan):
    total_harga = sum(harga * porsi for _, harga, porsi, _ in pesanan)
    return total_harga

def simpan_struk(pesanan, nama_pembeli, total_harga, uang_bayar, kembalian, waktu_sekarang):
    # Menulis informasi struk
    print("=================================================")
    print("|                 ANGKRINGAN MODERN             |")
    print("|           Jl. Semeru No. 6 Kota Tegal         |")
    print("=================================================")
    print(f" Tanggal        : {waktu_sekarang.year}-{waktu_sekarang.month}-{waktu_sekarang.day}")
    print(f" Jam            : {waktu_sekarang.strftime('%H:%M:%S')}")
    print(f" Nama Pembeli   : {nama_pembeli}")
    print("=================================================")

    tabel_struk_pesanan = PrettyTable()
    tabel_struk_pesanan.field_names = ["No", "Menu", "Harga", "Porsi", "Kategori"]
    for i, (menu, harga, porsi, kategori) in enumerate(pesanan, start=1):
        tabel_struk_pesanan.add_row([i, menu, harga, porsi, kategori])

    print(tabel_struk_pesanan)
    print("=================================================")

    print(f" Tagihan        : Rp. {total_harga}")

    while True:
        uang_bayar = int(input(" Uang           : Rp. "))
        if uang_bayar < total_harga:
            print("Uang yang dibayarkan kurang. Silakan masukkan nominal uang yang mencukupi.")
        else:
            break

    kembalian = uang_bayar - total_harga
    print(f" Kembalian      : Rp. {kembalian}")

    print("==================================================")
    print("|            TERIMA KASIH TELAH MEMBELI          |")
    print("|                DI ANGKRINGAN MODERN            |")
    print("==================================================")

def login_admin():
    print("""
-------------------------------------------------
          LOGIN ADMIN ANGKRINGAN MODERN
                    KOTA TEGAL
-------------------------------------------------
    """)
    # Set password yang benar
    password_benar = "admin"

    # Gunakan loop untuk meminta password hingga benar
    while True:
        user = input("Masukkan Username   : ")
        password = input("Masukkan Password   : ")

        if password == password_benar:
            print("Login berhasil.")
            return True
        else:
            print("Username atau Password salah. Silakan coba lagi.")
            continue

def main():
    if not login_admin():
        return

    print("""
-------------------------------------------------
        SELAMAT DATANG DI ANGKRINGAN MODERN
                    KOTA TEGAL
-------------------------------------------------
    """)

    nama_pembeli = input("Masukkan nama pembeli: ")

    tabel_menu_pesanan = PrettyTable()
    tabel_menu_pesanan.field_names = ["No", "Menu", "Harga"]

    # Daftar menu makanan
    daftar_menu_makanan = [
        ("Nasi Bakar", 7000),
        ("Nasi Kucing", 5000),
        ("Mie Goreng", 10000),
        ("Mie Rebus", 10000),
        ("Mendoan", 10000),
        ("Pepes Ayam", 4500),
        ("Sate Usus", 3000),
        ("Sate Ati", 3000),
        ("Sate Ampela", 3000),
        ("Sate Telur Puyuh", 3000),
        ("Sate Seafood", 3000),
        ("Sosis Bakar", 3000),
        ("Bakso Bakar", 3000),
    ]

    # Daftar menu minuman
    daftar_menu_minuman = [
        ("Es Teh", 3000),
        ("Teh Anget", 3000),
        ("Es Jeruk", 3500),
        ("Jeruk Anget", 4000),
        ("Es Kopi", 5000),
        ("Kopi Susu", 5000),
        ("Kopi Tubruk", 7000),
        ("Kopi Jos", 8000),
        ("Jahe Susu", 5000),
        ("Wedang Jahe", 5000),
    ]

    pesanan = []
    lanjut_pesan = True

    while lanjut_pesan:
        print("\nPilihan Menu:")
        print("1. Makanan")
        print("2. Minuman")

        kategori_menu = input("Pilih kategori menu (1/2): ")

        if kategori_menu == "1":
            tabel_menu_pesanan.clear_rows()
            tampilkan_tabel_menu(tabel_menu_pesanan, daftar_menu_makanan, "Menu Makanan")
        elif kategori_menu == "2":
            tabel_menu_pesanan.clear_rows()
            tampilkan_tabel_menu(tabel_menu_pesanan, daftar_menu_minuman, "Menu Minuman")
        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")
            continue

        input_nomor_menu = input("Pilih nomor menu yang dipisahkan oleh spasi: ")
        nomor_menu_list = [int(nomor) for nomor in input_nomor_menu.split()]

        for nomor_menu in nomor_menu_list:
            if 1 <= nomor_menu <= len(daftar_menu_makanan) and kategori_menu == "1":
                menu_dipesan = (daftar_menu_makanan[nomor_menu - 1][0], daftar_menu_makanan[nomor_menu - 1][1])
                porsi = int(input(f"Masukkan jumlah porsi untuk {menu_dipesan[0]}: "))
                pesanan.append((menu_dipesan[0], menu_dipesan[1], porsi, "Makanan"))
            elif 1 <= nomor_menu <= len(daftar_menu_minuman) and kategori_menu == "2":
                menu_dipesan = (daftar_menu_minuman[nomor_menu - 1][0], daftar_menu_minuman[nomor_menu - 1][1])
                porsi = int(input(f"Masukkan jumlah porsi untuk {menu_dipesan[0]}: "))
                pesanan.append((menu_dipesan[0], menu_dipesan[1], porsi, "Minuman"))
            else:
                print(f"Nomor menu {nomor_menu} tidak valid. Silakan pilih kembali.")
                continue

        jawab = input("Apakah Anda ingin memesan lagi? (ya/tidak): ")
        if jawab.lower() != "ya":
            lanjut_pesan = False

    waktu_sekarang = datetime.now()
    hari, bulan, tahun = waktu_sekarang.day, waktu_sekarang.month, waktu_sekarang.year
    waktu = waktu_sekarang.strftime("%H:%M:%S")

    total_harga = hitung_total_pesanan(pesanan)

    # Menampilkan struk pembayaran di terminal
    simpan_struk(pesanan, nama_pembeli, total_harga, 0, 0, waktu_sekarang)
    print(f"Struk pembayaran telah ditampilkan.")

if __name__ == "__main__":
    main()
