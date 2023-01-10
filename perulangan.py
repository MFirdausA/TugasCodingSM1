print("====PERHITUNGAN GAJI====")
print()

Jam_kerja = int(input("Berapa jam kerja kamu: "))

if Jam_kerja >= 12:
    print("Gaji kamu adalah 2800000")
elif Jam_kerja >= 8:
    print("Gaji kamu adalah 2500000")
elif Jam_kerja < 8:
    print("Aduh kamu ga dapet gaji")
else:
    print("Masukan dengan jujur")

print()

print("===Kriteria Nilai====")

print()

Nilai = int(input("Masukan Nilai Kamu: "))

if Nilai >=90 and Nilai <=100:
    print("Maka nilai kamu adalah A")
elif Nilai  >=80 and Nilai <90:
    print("Maka Nilai Kamu adalah B")
elif Nilai >= 70 and Nilai <80:
    print("Maka Nilai Kamu adalah C")
elif Nilai >= 60 and Nilai <70:
    print("Maka Nilai Kamu adalah D")
elif Nilai < 60:
    print("Maka Nilai Kamu adalah E")
else:
    print("Kelebihan/Nilai Tidak benar")