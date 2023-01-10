print("====APP PEMESANAN FOOD CORNER BPI====")

pilihan1=1
potongan_harga = -2000
jmlh_item=int(input("Mau Beli Berapa Item: "))
if pilihan1 == 1:
    for i in range(jmlh_item):
        i+= 1
        print(i)
        print("Pilihan item")
        print("1.Makanan berat [Potongan Rp.2000 ALL Item]")
        print("2.Makanan ringan")
        print("3.Minuman")
        Pilihan_Nomor =int(input("Pilihan Nomor: "))
        Nama_item = str(input("Nama Item: "))
        Harga_item = int(input("Harga Item: "))
        potongan=Harga_item-potongan_harga
        print("Item 1:",Pilihan_Nomor)
        print("Harga:",Harga_item)
        print("potongan harga",potongan)
        total = potongan_harga + Harga_item
        print("Total: ",total)


#input pilihan item
#output barang1
#output barang2
#output barang3
#input pilihan1
#input nama item
#input harga
#ouput pilihan barang
#output potongan harga dari barang 1
#output harga