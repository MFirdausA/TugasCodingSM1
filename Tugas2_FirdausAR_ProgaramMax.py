print("====Progaram Menentukan max====")

bilangan1=int(input("MASUKAN BILANGAN 1: "))
bilangan2=int(input("MASUKAN BILANGAN 2: "))
bilangan3=int(input("MASUKAN BILANGAN 3: "))

if bilangan1 > bilangan2:
    hasil= bilangan1
elif bilangan2 > bilangan3:
    hasil= bilangan2
elif bilangan3 > bilangan2:
    hasil= bilangan3

print("BILANGAN TERBESAR ADAKAH",hasil)