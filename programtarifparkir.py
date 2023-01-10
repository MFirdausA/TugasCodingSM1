print("====================================")
print("=                                   =")
print("=        TARIF PARKIR               =")
print("=                                   =")
print("=====================================")

masuk=int(input("Jam masuk anda parkir: "))
keluar=int(input("jam keluar anda parkir: "))
payment=3500
lama_parkir=keluar-masuk
print("=====================================")
print(f"durasi: {lama_parkir}")
if lama_parkir<=1:
    satu_jam_pertama=payment
    print("Tarif= Rp,",satu_jam_pertama)
elif lama_parkir<12:
    tarif_selanjutnya= (lama_parkir-1)*2000+payment
    print("Tarif= Rp",tarif_selanjutnya)
elif lama_parkir>12:
    tarif_selanjutnya = (lama_parkir - 1) * 2000 + payment
    print("Tarif= Rp", tarif_selanjutnya)
elif lama_parkir<=24:
    tarif_selanjutnya = (lama_parkir - 1) * 2000 + payment
    print("Tarif= Rp", tarif_selanjutnya)
else:
    print("error")