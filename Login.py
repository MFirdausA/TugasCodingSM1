print("====LOGIN USER====")

username="ayam123"
password="ayam321"

username=input("MASUKAN USERNAME ANDA: ")
password=input("MASUKAN PASSWORD ANDA: ")

if username=="ayam123" and password=="ayam321":
    print("selamat datang")
else:
    print("username anda salah")

#cara ke2
if username==username:
    if password==password:
        print("welcome")
    else:
        print("password salah")
else:
    print("username salah")