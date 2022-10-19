var = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
tamp = 0
inp = str(input("Masukkan Angka Romawi : ")).upper()
for i in range(len(inp)):
    if i == 0 or var[i] <= var[i-1]:
        tamp += var[i]
    else:
        tamp += var[i]-2*var[i-1]
print(tamp)