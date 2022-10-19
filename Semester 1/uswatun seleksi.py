ta = int(input("Masukkan TA : "))
tk = int(input("Masukkan TK : "))
tp = int(input("Masukkan TP : "))
rerata = (ta+tk+tp)/3
if rerata >= 75:
    print("Nilai Rata - Rata :",rerata)
    if tk < ta > tp:
        print("bagian Administrasi")
    elif ta < tk > tp:
        print("Bagian Produksi")
    else:
        print("Bagian Administrasi")
else:
    print("Nilai Rata - Rata :",rerata)
    print("Anda Tidak LULUS")