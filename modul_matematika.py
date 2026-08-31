def ganjilgenap(x): 
    while True: 
        x = int(input("Masukkan angka :"))
        if x % 2 == 0:
            print("genap") 
        else:
            print("ganjil")

def bilanganprima(n):
    while True:
        n = int(input("Masukkan angka :"))    
        if n <= 1:
            print(n, "bukan bilangan prima")
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                print(n, "bukan bilangan prima")
                return False
        print(n, "adalah bilangan prima")
        return True