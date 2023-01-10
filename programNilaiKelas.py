print("==== PROGRAM NILAI KELAS X-RPL====")

input_nilai_siswa = int(input("mau input berapa nilai?: "))
rata_kelas = 0
if input_nilai_siswa == 0:
    print("Input nilai yang di masukan minimal 1")
else:
    for i in range(input_nilai_siswa):
        i += 1
        print(i)
        nama = str(input("Nama Siswa: "))
        tugas = float(input("Nilai Tugas: "))
        harian = float(input("Nilai Harian: "))
        pts = float(input("Nilai PTS: "))
        pas = float(input("Nilai PAS: "))
        print('-' * 20)
        print("Nama Siswa:", nama)
        jumlah_nilai = tugas + harian + pts + pas
        ratarata = jumlah_nilai / 4
        print("Jumlah Nilai:", jumlah_nilai)
        print("Rata-rata Nilai:", ratarata)
        print()
        print("=======================")
        rata_kelas = ratarata / input_nilai_siswa
    print("Rata-rata Nilai Kelas", rata_kelas)

# STRUKTUR ALGORITMA#
# OUTPUT JUDULZ
# INPUT BANYAK PERULANGAN
# DI DALAM PERULANGAN:
    # (if input_nilai_siswa == 0:
    # print("Banyak nilai tidak boleh kosong"))
    # NOMOR
    # INPUT NAMA SISWA
    # INPUT NILAI TUGAS
    # INPUT NILAI HARIAN
    # INPUT NILAI PTS
    # INPUT NILAI PAS
    # OUTPUT NAMA SISWA
    # OPERSI HITUNG JML SISWA
    # OPERASI HITUNG RATA NILAI
    # OUTPUT JML NILAI
    # OUPUT RATA NILAI
# OPERASI RATA KELAS
# OUTPUT RATA KELAS