print("====CALCULATOR====")
#deklasrasi variabel input  angka1,angka2
#proses penjumlahan ditampung ke dalam variabel hasil =angka1 + angka2
#output angka 1 + angka 2 hasil

#Deklasrasi
Angka1=int(input("Masukan angka:"))
Angka2=int(input("Masukan angka:"))

#Proses
Hasil= Angka1 + Angka2
Hasil1= Angka1 - Angka2
Hasil2= Angka1 * Angka2
Hasil3= Angka1 / Angka2
Hasil4= Angka1 % Angka2
Hasil5= Angka1 ** Angka2
Hasil6= Angka1 // Angka2


#Output

print(f"{Angka1}-{Angka2}={Hasil1}")
print(f"{Angka1}*{Angka2}={Hasil2}")
print(f"{Angka1}/{Angka2}={Hasil3}")
print(f"{Angka1}%{Angka2}={Hasil4}")
print(f"{Angka1}**{Angka2}={Hasil5}")
print(f"{Angka1}//{Angka2}={Hasil6}")