n = int(input("Masukkan Size : "))
for i in range(n+1):
    if i == 0 or i == n:
        print(i," "+"x"*n)
    elif i == (n//2):
        print(i," "+"x"*n)
    else:
        print(i,"x"+" "*(n)+"x")

# while True:
#     n = int(input("Masukkan Size : "))
#     for i in range(1,n+1):
#         print(i,"*"*i)
#     a = str(input("Mau ULang? (y/t) : ")).lower()
#     print(a)
#     if a == 'y':
#         continue
#     else:
#         break

a = 'kalimat tanya'
print(a.title())
print(a.lower())
print(a.upper())