n = int(input("masukkan bilangan desimal: "))
basis = int(input("masukkan basis tujuan konversi: "))

hasil = ""

while n!=0:
    sisa = n % basis
    print("{} / {} = {}, sisa {}".format(n,basis,(n//basis),sisa))
    n = n // basis
    hasil = hasil + str(sisa)

print("hasil konversi:",hasil[::-1])