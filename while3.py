print("====== BELAJAR PERULANGAN WHILE 3 ======")
i=0
jumlah=0

angka=int(input("Mau mengulang berapa kali:"))
for i in range (1,angka+1):

    jumlah=jumlah+i
    print("Memanggil",i,"Kali")

print("Jumlah memanggil=",jumlah,"kali")