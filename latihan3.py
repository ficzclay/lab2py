# Input nilai variabel
a = input("Masukkan nilai a:")
b = input("Masukkan nilai b:")

# Cetak nilai variabel
print("Variabel a =", a)
print("Variabel b =", b)

# Cetak hasil operasi kedua variabel dengan String Format
print("Hasil penggabungan {}+{}={}".format(a, b, a + b))

# Konversi nilai variabel
a = int(a)
b = int(b)
print("Hasil penjumlahan {}+{}={}".format(a, b, a + b))
print("Hasil pembagian {}/{}={:.2f}".format(a, b, a / b))
