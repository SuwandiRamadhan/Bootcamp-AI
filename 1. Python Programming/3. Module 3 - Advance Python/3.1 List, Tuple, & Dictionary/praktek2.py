# Tuple
# ingat bahwa tuple bersifat immutable, yang berarti isi tuple tidak bisa diubah/diupdate

tuple1 = ('apple', 'banana', 'cherry')
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ('apple', 1, 3.0, False)

# Cara akses tuple sama seperti list
fruitTuple = ('apple', 'banana', 'watermelon', 'orange', 'mango')
print(fruitTuple[2])
print(fruitTuple[1:3])
print(fruitTuple[-2:]) # Mengambil 2 elemen terakhir

'''
fruitTuple[2] = 'melon' # Tuple bersifat immutable, tidak bisa diubah/diupdate

# ini akan menghasilkan error
'''


# Dictionary
# Dictionary adalah tipe data yang berisi pasangan key-value

fruitDict = {
                'nama' : 'apple',
                'warna' : 'merah',
                'kode' : 101,
                'harga' : 10000
            }
print(fruitDict['kode'])
print(fruitDict)

fruitDict['harga'] = 15000 # Mengubah
print(fruitDict)


# Looping di dalam tuple
for x in tuple1:
    print(x)

# Looping di dalam dictionary
for key, value in fruitDict.items():
    print(key, value)

for key in fruitDict.keys():
    print(key, fruitDict[key])


# SET
# Set adalah tipe data yang berisi kumpulan item bersifat unik dan tanpa urutan (unordered collection)
# Set menggunakan kurung kurawal {} tapi tanpa pasangan key-value

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Union (gabungan)
print(A | B)

# Intersection (irisan)
print(A & B)

# Difference (selisih) sama seperti left dan right join di SQL
print(A - B)
print(B - A)
 
# Symmetric Difference (selisih simetris)
print(A ^ B)
















