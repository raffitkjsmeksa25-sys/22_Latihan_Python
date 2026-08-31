def ganjilgenap(x):
    while True:
        x = int(input("Masukkan angka :"))
        if x % 2 == 0:
            print("genap")
        else:
            print("ganjil")

if __name__ == "__main__":
    ganjilgenap()
    
