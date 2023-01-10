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

if lama_parkir+12 and lama_parkir >=0:
    satu_jam_pertama= (lama_parkir-1)*2000+payment
    print("lama parkir= ", lama_parkir, "jam")
    print('Tarif= Rp', satu_jam_pertama)
elif lama_parkir+12 and lama_parkir>=0:
    print("Tarif= Rp" , 42000)
else:
    print("Jam masuk harus bernilai antara 1 - 12")
