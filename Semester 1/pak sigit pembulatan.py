x = int(input("Masukkan Angka => "))
s = x % 5
if x > 40:
    if x % 5 < 3:
        if s == 0:
            x = x
        elif s == 2:
            x -= 2
        else:
            x -= 1
    else:
        if s == 4:
            x += 1
        else:
            x += 2
else:
    print("Pembulatan :",x)

print("Pembulatan :",x)