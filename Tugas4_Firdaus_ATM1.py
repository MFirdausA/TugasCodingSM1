print("====Program ATM====")
print("")
saldo = 1000000
print("saldo anda adalah", saldo)
nominal_penarikan = int(input("masukan nominal yang ingin anda tarik: "))

if nominal_penarikan < saldo:
    sisa_saldo = saldo - nominal_penarikan
    print("sisa saldo anda adalah", sisa_saldo)
    print("saldo cukup")
else:
    print("saldo tidak cukup")
