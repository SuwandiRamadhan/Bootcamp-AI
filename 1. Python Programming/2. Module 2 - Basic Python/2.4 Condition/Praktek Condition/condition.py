# Condition IF

print("\n")
jumlahPenumpang = 13

if jumlahPenumpang > 10:
    print("Mobil akan berjalan")

if jumlahPenumpang < 10:
    print("Mobil tidak akan berjalan")

print("Di luar condition")


# Condition ELSE IF
print("\n")

score = 80

if score >= 80:
    print("Selamat, Anda lulus!")
elif score >= 70:
    print("Anda hampir lulus!")
else:
    print("Anda tidak lulus")


# Nested IF (IF bersarang)
print("\n")

kelas = 5
score = 90

if kelas > 1:
    if score >= 85:
        print("Predikat A / Memuakan")
    elif score >= 75:
        print("Predikat B / Bagus")
    else:
        print("Predikat C / Cukup")
else:
    if score >= 80:
        print("Predikat A / Bagus")
    else:
        print("Tidak lulus")


# Tambahan

num = float(input("Masukkan angka: "))

if num >= 0:
    if num == 0:
        print("Nol")
    else:
        print("Bilangan positif")

















