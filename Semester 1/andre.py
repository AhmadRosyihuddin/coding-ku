gaji = int(input("Masukkan Gaji => "))
rumah = str(input("Apakah memiliki Rumah? (ya/tidak) => ")).lower()
nikah = str(input("Sudah Menikah? (ya/tidak) => ")).lower
if gaji > 3:
    print("Wajib Mengikuti Asuransi")
else:
    print("Tidak Wajib Mengikuti Asuransi")

if nikah == 'ya':
    print("Boleh Menabung")
else:
    print("Tidak Boleh Menabung")

if rumah == 'ya':
    print("Membayar Pajak")
else:
    print("Tidak membayar Pajak")  