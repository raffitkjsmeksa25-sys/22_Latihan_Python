import modul_matematika
import ganjil_genap

print("1. Program Ganjil Genap\n2. Program Bilangan Prima")

pilihprogram = input("Pilih program yang ingin dijalankan (1/2): ")
if pilihprogram == "1":
    x = 0  # Inisialisasi variabel x
    modul_matematika.ganjilgenap(x)
elif pilihprogram == "2":
    n = 0  # Inisialisasi variabel n
    modul_matematika.bilanganprima(n)

