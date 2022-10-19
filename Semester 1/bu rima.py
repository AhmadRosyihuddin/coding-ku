def deret(a,b,n):
    if n == 1:
        return a
    else:
        print(n,'b + deret(a,b,n-1)')
        q = b + deret(a,b,n-1)
        print(n)
        return q

hasil = deret(2,3,6)
print(hasil)
