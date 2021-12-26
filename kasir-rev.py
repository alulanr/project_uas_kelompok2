import os
from datetime import datetime

current = datetime.now()
tahun = current.year
bulan = current.month
hari = current.day
import datetime
x = datetime.datetime.now()
waktu = (x.strftime("%H:%M:%p"))

ulangah="y"
while ulangah=="y":
    print("""
------------------------------------------------------------
                LOGIN ADMIN ANGKRINGAN MODERN
                        KOTA TEGAL
------------------------------------------------------------
Silahkan Masukkan Username dan Password
Pass admin
    """)
    user=input("Masukkan Username   : ")
    password=input("Masukkan Password   : ")
    if password=="admin":
        ulangin="y"
        while ulangin=="y":
            print("""
------------------------------------------------------------
            SELAMAT DATANG DI ANGKRINGAN MODERN
                        KOTA TEGAL
------------------------------------------------------------
1. Menu Angkringan Modern
2. Logout
------------------------------------------------------------
            """)
            pilih = input("Pilih sesuai kebutuhan Anda : ")

# Start Menu
            if pilih == "1" or pilih == "menu":
                ripit = "ok"
                while ripit == "ok":
                    print("""

------------------------------------------------------------
            SELAMAT DATANG DI ANGKRINGAN MODERN
                        KOTA TEGAL
------------------------------------------------------------

------------------------------------------------------------
                 Kasir Angkringan Modern          
------------------------------------------------------------

""")
                    pembeli = input("Nama Pembeli   : ")

                    print("""

~ Menu Makanan ~                             |    ~ Menu Minuman ~
1. Nasi Bakar             - Rp 7.000,-         |    1. Es Teh      - Rp 3.000,-
2. Nasi Kucing            - Rp 5.000,-         |    2. Teh Anget   - Rp 2.500,-
3. Indomie Goreng / Rebus - Rp 8.000,-         |    3. Es Jeruk    - Rp 3.500,- 
4. Mendoan                - Rp 10.000,-        |    4. Jeruk Anget - Rp 4.000,-
5. Pepes Ayam             - Rp 4.500,-         |    5. Es Kopi     - Rp 4.500,-
6. Sate Usus              - Rp 3.000,-         |    6. Kopi Susu   - Rp 4.000,-
7. Sate Ati               - Rp 3.000,-         |    7. Kopi Tubruk - Rp 4.000,-
8. Sate Ampela            - Rp 3.000,-         |    8. Kopi Jos    - Rp 5.000,-
9. Sate Telur Puyuh       - Rp 3.000,-         |    9. Jahe Susu   - Rp 5.000,-
10. Sate Seafood          - Rp 2.000,-         |    10. Wedang Jahe - Rp 4.000,-
11. Sate Kulit            - Rp 3.000,-         |    
12. Sosis Bakar           - Rp 3.000,-         |    
13. Bakso Bakar           - Rp 3.000,-         |  

00. Kembali Ke Awal
""")
   
                    banyak_pesan = int(input("Banyak Pesanan : "))
                    if banyak_pesan > 13:
                        print("\nMenu tidak ada, silahkan pilih lagi")
                        ripit = "ok"
                        break
                    

                    uang      = [0]
                    kembalian = [0]
                    
                    total_minuman = 0
                    jenis_minuman = ""
                    porsi = 0
                    gelas = 0

                    total_makanan = 0
                    jenis_makanan = ""
                    total_minuman = 0
                    jenis_minuman = ""
                    totalsemua = 0
                    totalsemua = ""

                    i = 0
                    for i in range(banyak_pesan):
                        print("Pesanan ke - ", i+1)
                        nomor_makanan = (int(input("\nPilihan Makanan : ")))
                        porsi = (int(input("Berapa Porsi    : ")))
                        nomor_minuman = (int(input("Pilihan Minuman : ")))
                        gelas = (int(input("Berapa Gelas    : ")))

                        i += 1

                        def fungsimakanan():
                            global nomor_makanan
                            global total_makanan
                            global jenis_makanan
                            global porsi
                            if (nomor_makanan == 1):
                                total_makanan = (porsi * 7000)
                                print (porsi," porsi Nasi Bakar = Rp", total_makanan)
                                jenis_makanan = ("Nasi Bakar")
                            elif (nomor_makanan == 2):
                                total_makanan = (porsi * 5000)
                                print (porsi," porsi Nasi Kucing = Rp", total_makanan)
                                jenis_makanan = ("Nasi Kucing")
                            elif (nomor_makanan == 3):
                                total_makanan = (porsi * 8000)
                                print (porsi, " porsi Indomie Goreng / Rebus = Rp", total_makanan)
                                jenis_makanan = ("Indomie Goreng / Rebus")
                            elif (nomor_makanan == 4):
                                total_makanan = (porsi * 10000)
                                print (porsi, " porsi Mendoan = Rp", total_makanan)
                                jenis_makanan = ("Mendoan")
                            elif (nomor_makanan == 5):
                                total_makanan = (porsi * 4500)
                                print (porsi, " Pepes Ayam = Rp", total_makanan)
                                jenis_makanan = ("Pepes Ayam")
                            elif (nomor_makanan == 6): 
                                total_makanan = (porsi * 3000)
                                print (porsi, " Sate Usus = Rp", total_makanan)
                                jenis_makanan = ("Sate Usus")
                            elif (nomor_makanan == 7):
                                total_makanan = (porsi * 3000)
                                print (porsi, " Sate Ati = Rp", total_makanan)
                                jenis_makanan = ("Sate Ati")
                            elif (nomor_makanan == 8):
                                total_makanan = (porsi * 3000)
                                print (porsi ," Sate Ampela = Rp", total_makanan)
                                jenis_makanan = ("Sate Ampela")
                            elif (nomor_makanan == 9):
                                total_makanan = (porsi * 3000)
                                print (porsi, " Sate Telur Puyuh = Rp", total_makanan)
                                jenis_makanan = ("Sate Telur Puyuh")
                            elif (nomor_makanan == 10):
                                total_makanan = (porsi * 2000)
                                print (porsi, " Sate Seafood = Rp", total_makanan)
                                jenis_makanan = ("Sate Seafood")
                            elif (nomor_makanan == 11):
                                total_makanan = (porsi * 3000)
                                print (porsi, " Sate Kulit = Rp", total_makanan)
                                jenis_makanan = ("Sate Kulit")
                            elif (nomor_makanan == 12): 
                                total_makanan = (porsi * 3000)
                                print (porsi, " Sosis Bakar = Rp", total_makanan)
                                jenis_makanan = ("Sosis Bakar")
                            elif (nomor_makanan == 13):
                                total_makanan = (porsi * 3000)
                                print (porsi, " Baso Bakar = Rp", total_makanan)
                                jenis_makanan = ("Baso Bakar")           
                            else:
                                total_makanan = (porsi * 0)
                                jenis_makanan = ("Pilihan tidak ada, silahkan masukan lagi!!")   

                        def fungsiminuman():
                            global nomor_minuman
                            global total_minuman
                            global jenis_minuman
                            global gelas
                            if (nomor_minuman == 1):
                                total_minuman = (gelas * 3000)
                                print (gelas," Gelas Es Teh = Rp", total_minuman)
                                jenis_minuman = ("Gelas Es Teh")
                            elif (nomor_minuman == 2):
                                total_minuman = (gelas * 2500)
                                print (gelas, " Gelas Teh Anget = Rp", total_minuman)
                                jenis_minuman = ("Teh Anget")
                            elif (nomor_minuman == 3):
                                total_minuman = (gelas * 3500)
                                print (gelas, " Gelas Es Jeruk = Rp", total_minuman)
                                jenis_minuman = ("Es Jeruk")
                            elif (nomor_minuman == 4):
                                total_minuman = (gelas * 4000)
                                print (gelas, " Gelas Jeruk Anget = Rp", total_minuman)
                                jenis_minuman = ("Jeruk Anget")
                            elif (nomor_minuman == 5):
                                total_minuman = (gelas * 4500)
                                print (gelas, " Gelas Es Kopi = Rp", total_minuman)
                                jenis_minuman = ("Es Kopi")
                            elif (nomor_minuman == 6):
                                total_minuman = (gelas * 4000)
                                print (gelas, " Gelas Kopi Susu = Rp", total_minuman)
                                jenis_minuman = ("Kopi Susu")
                            elif (nomor_minuman == 7):
                                total_minuman = (gelas * 4000)
                                print (gelas, " Gelas Kopi Tubruk = Rp", total_minuman)
                                jenis_minuman = ("Kopi Tubruk")
                            elif (nomor_minuman == 8):
                                total_minuman = (gelas * 5000)
                                print (gelas, " Gelas Kopi Jos = Rp", total_minuman)
                                jenis_minuman = ("Kopi Jos")
                            elif (nomor_minuman == 9):
                                total_minuman = (gelas * 5000)
                                print (gelas, " Gelas Jahe Susu = Rp", total_minuman)
                                jenis_minuman = ("Jahe Susu")
                            elif (nomor_minuman == 10):
                                total_minuman = (gelas * 4000)
                                print (gelas, " Gelas Wedang Jahe = Rp", total_minuman)
                                jenis_minuman = ("Wedang Jahe")   
                            else:
                                total_minuman = (porsi * 0)
                                jenis_minuman = ("Pilihan tidak ada, silahkan masukan lagi!!")   
                        
                        i += 1
                         
                        def order_jadi():
                            global total_makanan
                            global total_minuman
                            global totalsemua
                            totalsemua = (total_makanan + total_minuman)
                            print("\nTotal harus Dibayar : Rp",totalsemua)
                            uang = int(input("Uang Tunai Pembeli  : Rp "))
                            kembalian = int(uang - totalsemua)
                            print("Kembalian  :",kembalian)

                            

                            os.system('cls')

            
                            print("-------------------------------------")
                            print("|         ANGKRINGAN MODERN         |")
                            print("|    Jl. Semeru No. 6 Kota Tegal    |")
                            print("-------------------------------------")
                            print(" Tanggal    :"" {}/{}/{}                ".format(hari, bulan, tahun))
                            print(" Jam        :",waktu)
                            print(" Nama       :",pembeli)
                            print("=====================================")

                            if(porsi <= 0 ):
                                print (" Beli       : Tidak membeli makanan")
                                print ("             ",gelas,jenis_minuman,"-", total_minuman)
                            elif(gelas <= 0):
                                print (" Beli       :",porsi,jenis_makanan,"-", total_makanan)
                                print (" Beli       : Tidak membeli minuman")
                            else:
                                print (" Beli       :",porsi,jenis_makanan,"-", total_makanan)
                                print ("             ",gelas,jenis_minuman,"-", total_minuman)

                                print("_____")
                                print("              Tagihan    : Rp.",totalsemua)
                                print("              Uang       : Rp.",uang)
                                print("              Kembalian  : Rp.",kembalian)
                                print("=====================================")
                                print("|    TERIMA KASIH TELAH MEMBELI     |")
                                print("|       DI ANGKRINGAN MODERN        |")
                                print("=====================================")
                                
                        
                        fungsimakanan()
                        fungsiminuman()
                        order_jadi()
                        os.system('exit')
                                        

# Kembali Logout
            elif pilih == "4" or pilih == "ulang":
                ulangin = "y"
                break
            else:
                ulangin=input("Pilihan tidak ada apakah anda ingin mengulangi (y/n) : ")
    else:
        print("\nPassword salah!\n")
        ulangin=input("Apakah anda ingin login kembali (y/n) : ")
        if ulangin== "n":
            exit()
        else:
            os.system('exit')
                            
            exit()
