import os

print("===========================================")
print("=== SELAMAT DATANG DI ANGKRINGAN MODERN ===")
print("===========================================")
print("\n-------------------------------------------")
print("          Kasir Angkringan Modern          ")
print("-------------------------------------------")
pembeli = input("Nama Pembeli : ")
pertanyaan_makanan = input("Mau pesan Makan? ")
pertanyaan_minuman = input("Mau pesan Minum? ")

def fungsimakanan():
   global total_makanan
   global porsi
   global jenis_makanan
   print("\n~~ Menu Makanan ~~")
   print("1. Nasi Goreng - Rp 15.000,-")
   print("2. Soto - Rp 10.000,-")
   print("3. Mie Ayam - Rp 10.000,-")
   print("4. Nasi Kucing - Rp 5.000,-")
   print("5. Sate Usus - Rp 2.000,-")
   print("6. Sate Seafood - Rp 2.000,-")
   print("7. Mendoan - Rp 10.000,-")
   print("")
   nomor = int(input("Masukan Pilihan : "))
   porsi = int(input("Berapa Porsi    : "))
   
   os.system('cls')

   if nomor == 1:
       total_makanan = porsi * 15000
       print (porsi," porsi Nasi Goreng = Rp", total_makanan)
       jenis_makanan = "Nasi Goreng"
   elif nomor == 2:
       total_makanan = porsi * 10000
       print (porsi," porsi Soto = Rp", total_makanan)
       jenis_makanan = "Soto"
   elif nomor == 3:
       total_makanan = porsi * 10000
       print (porsi, " porsi Mie Ayam = Rp", total_makanan)
       jenis_makanan = "Mie Ayam"
   elif nomor == 4:
       total_makanan = porsi * 5000
       print (porsi, " porsi Nasi Kucing = Rp", total_makanan)
       jenis_makanan = "Nasi Kucing"
   elif nomor == 5:
       total_makanan = porsi * 2000
       print (porsi, " Sate Usus = Rp", total_makanan)
       jenis_makanan = "Sate Usus"
   elif nomor == 6: 
       total_makanan = porsi * 2000
       print (porsi, " Sate Seafood = Rp", total_makanan)
       jenis_makanan = "Sate Seafood"
   elif nomor == 7:
        total_makanan = porsi * 10000
        print (porsi, " Mendoan = Rp", total_makanan)
        jenis_makanan = "Mendoan"       
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsimakanan()

      os.system('cls')

def fungsiminuman():
   global total_minuman
   global gelas
   global jenis_minuman
   print("\n~~ Menu Minuman ~~")
   print("1. Es Teh - Rp 3.000,-")
   print("2. Teh Anget - Rp 2.500,-")
   print("3. Es Jeruk - Rp 3.500,-")
   print("4. Es Kopi - Rp 4.000,-")
   print("5. Jahe Susu - Rp 5.000,-")
   print("")
   nomor = int(input("Masukan Pilihan: "))
   gelas = int(input("Berapa Gelas   : "))

   os.system('cls')

   if nomor == 1:
       total_minuman = gelas * 3000
       print (gelas," Es Teh = Rp", total_minuman)
       jenis_minuman = "Gelas Es Teh"
   elif nomor == 2:
       total_minuman = gelas * 2500
       print (gelas, " Gelas Teh Anget = Rp", total_minuman)
       jenis_minuman = "Teh Anget"
   elif nomor == 3:
       total_minuman = gelas * 3500
       print (gelas, " Es Jeruk = Rp", total_minuman)
       jenis_minuman = "Es Jeruk"
   elif nomor == 4:
       total_minuman = gelas * 4000
       print (gelas, " Gelas Es Kopi = Rp", total_minuman)
       jenis_minuman = "Es Kopi"
   elif nomor == 5:
       total_minuman = gelas * 5000
       print (gelas, " Gelas Jahe Susu = Rp", total_minuman)
       jenis_minuman = "Jahe Susu"     
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsiminuman()

      os.system('cls')

def order_jadi():
    totalsemua = total_makanan + total_minuman
    print("\nTotal harus Dibayar : Rp",totalsemua)
    uang = int(input("Uang Tunai Pembeli  : Rp "))
    kembalian = int(uang - totalsemua)
    print("Kembalian  :",kembalian)

    os.system('cls')

    print("-------------------------------------")
    print("|         ANGKRINGAN MODERN         |")
    print("-------------------------------------")
    print("=====================================")
    print("=== S T R U K   P E M B E L I A N ===")
    print("=====================================")
    print (" Nama       :",pembeli)

    if(porsi <= 0 ):
        print (" Beli       : Tidak membeli makanan")
        print ("             ",gelas,jenis_minuman,"-", total_minuman)
    elif(gelas <= 0):
        print (" Beli       :",porsi,jenis_makanan,"-", total_makanan)
        print (" Beli       : Tidak membeli minuman")
    else:
        print (" Beli       :",porsi,jenis_makanan,"-", total_makanan)
        print ("             ",gelas,jenis_minuman,"-", total_minuman)

    print(" Tagihan    : Rp.",totalsemua)
    print(" Uang       : Rp.",uang)
    print(" Kembalian  : Rp.",kembalian)
    print("=====================================")
    print("|    TERIMA KASIH TELAH MEMBELI     |")
    print("|       DI ANGKRINGAN MODERN        |")
    print("=====================================")

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

os.system('cls')

if (pertanyaan_makanan == 'tidak' or pertanyaan_makanan == 't') and (pertanyaan_minuman == 'tidak' or pertanyaan_minuman == 't'):
    print('Ngapain kesini ?')
elif pertanyaan_makanan == 'tidak' or pertanyaan_makanan == 't':
    fungsiminuman()
    order_jadi()
elif pertanyaan_minuman == 'tidak' or pertanyaan_minuman == 't':
    fungsimakanan()
    order_jadi()
else:
    fungsimakanan()
    fungsiminuman()
    order_jadi()