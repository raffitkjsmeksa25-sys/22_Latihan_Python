def ganjilgenap(x):
    if x % 2 == 0:
        print(x, "adalah bilangan genap")
    else:
        print(x, "adalah bilangan ganjil")


def bilanganprima(n):
    if n <= 1:
        print(n, "bukan bilangan prima")
        return

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(n, "bukan bilangan prima")
            return

    print(n, "adalah bilangan prima")
