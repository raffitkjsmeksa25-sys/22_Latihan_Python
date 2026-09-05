import modul_matematika

while True:
    print("\n===== MENU UTAMA =====")
    print("1. Program Ganjil Genap")
    print("2. Program Bilangan Prima")
    print("3. Exit")
    print("======================")

    pilihanprogram = input("Pilih program (1/2/3): ")

    if pilihanprogram == "1":
        x = int(input("Masukkan angka : "))
        modul_matematika.ganjilgenap(x)

    elif pilihanprogram == "2":
        n = int(input("Masukkan angka : "))
        modul_matematika.bilanganprima(n)

    elif pilihanprogram == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")