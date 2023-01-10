print("====pemograman ganjil genap====")
print()

bilangan = int(input("Masukan Bilangan: "))

if bilangan % 2 == 0:
    print("bilangan Genap")
else:
    print("Bilangan ganjil")

print("====PERHITUNGAN GAJI====")
print()

Jam_kerja = int(input("Berapa jam kerja kamu: "))

if Jam_kerja >= 12:
    print("Gaji kamu adalah 2.800.000")
elif Jam_kerja >= 8:
    print("Gaji kamu adalah 2.500.000")
elif Jam_kerja < 8:
    print("Aduh kamu ga dapet gaji")
else:
    print("Masukan dengan jujur")
