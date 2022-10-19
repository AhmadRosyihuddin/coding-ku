while True:
    n = int(input("Masukkan Size : "))
    for i in range(n+1):
        print(" "*(n//2)+"x")
    print()

    for i in range(n+1):
        if i == 0 or i == n:
            print("x"*n)
        elif i == (n//2):
            print("x"*n)
        elif i > (n//2):
            print("x")
        else:
            print(" "*(n-1)+"x")
    print()

    for i in range(n+1):
        if i == 0 or i == n:
            print("x"*n)
        elif i == (n//2):
            print("x"*n)
        elif i > (n//2):
            print("x"+" "*(n-2)+"x")
        else:
            print("x")

    a = str(input("Mau Ulang? (y/t) => ")).lower()
    if a == 'y':
        continue
    else:
        break