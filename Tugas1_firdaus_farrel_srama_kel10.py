print("=========program kasir sederhana=========")

barang1=input("barang1:")
harga1=int(input("harga:"))
barang2=input("barang2:")
harga2=int(input("harga:"))
barang3=input("barang3:")
harga3=int(input("harga:"))
uang=int(input("uang pelanggan :"))

print("1",barang1,"RP.",harga1)
print("2",barang2,"RP.",harga2)
print("3",barang3,"RP.",harga3)

Total=harga1+harga2+harga3
Total2=Total-(Total*20//100)

print(f"Total : {Total}")
print("dapat diskon 20%")
print('Harganya menjadi', Total2)
print(f"uang pelanggan {uang}")
print(f"kembalian {uang-Total2} ")

print("TERIMAKASIH TELAH BERBERLANJA DI SINI")


