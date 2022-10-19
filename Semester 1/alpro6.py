# konversi = lambda km: km*1000
# km = int(input('Masukkan Jarak (km) : '))
# print(km,'km =',konversi(km),'M')


def factorial(x):
    if x > 1:
        print(x)
        a = x * factorial(x-1)
        print(a)
        return a
    else:
        print(x)
        return 1
x = int(input('Masukkan Nilai faktorial : '))
print('Faktorial dari',x,':',factorial(x))

# Ilustrasi
#def factorial(4): = 24
#    if x > 1:
#        print(x) = 4
#        return 4 * factorial(4-1) = 6
#                    if x > 1:
#                        print(x) x = 3
#                        return 3 * factorial(3-1) = 2
#                        
#                            if x > 1:
#                                print(x) x = 2
#                                return 2 * factorial(2-1) = 1
#                                       
#                                       else:
#                                           return 1
#                                
#                                       