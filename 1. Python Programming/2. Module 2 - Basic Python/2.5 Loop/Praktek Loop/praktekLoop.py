# While Loop
count = 0

while (count < 9):
    print("Nilai count : ", count)
    count += 1
print("While loop selesai")
print('\n')

# For Loop
listAngka = [1, 2, 3, 4, 5]

for x in listAngka:
    print("Nilai x : ", x)
print("For loop selesai")
print('\n')

# Tambahan For Loop
print(range(5))
print(list(range(1, 23, 3))) # pertama untuk start, kedua untuk stop, ketiga untuk step(lompatan)
print('\n')

for x in list(range(1, 11)):
    print("Nilai x : ", x)
print("For loop selesai")


# Nested Loop
i = 90

while (i < 100):
    j = 2
    print(i/j)
    while(j <= i/j):
        print("ini loop di dalam loop")
        j += 1
        i += 1
print("Selesai")


# Break dan Continue
for i in "string":
    if i == "i":
        break
    print(i)
print('\n')

for i in "string":
    if i == "i":
        continue
    print(i)


# For Else

daftarMurid = ["Ali", "Budi", "Dedi"]

namaMurid = "Ali"

for nama in daftarMurid:
    if nama == namaMurid:
        print(nama)
        break
else:
    print("Murid tidak ada di dalam daftar murid")


# Pass
    for nama in daftarMurid:
        pass
    
    if nama == namaMurid:
        pass
    else:
        pass
    
# jadi kita bisa isi pass pass dulu sebelum input nilai asli untuk menghindari error
# pass itu seperti tempat kosong yang bisa diisi dengan kode lainnya















