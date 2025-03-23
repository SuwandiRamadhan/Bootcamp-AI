'''
list = []
tuple = ()
dictionary = {}
set = {} #set tidak menyertakan key value
'''


# List =====================================================================================================

# Menambahakan list
# list.append() = Menambahkan elemen di akhir list
namaKucing = ['Browny', 'Snowy', 'Blacky']
namaKucing.append('Nuna')
print(namaKucing)

# list.insert() = Menambahkan elemen di tengah posisi yang diinginkan
namaKucing.insert(1, 'Kitty')
print(namaKucing)

# list.extend() = Menambahkan elemen list ke list lain
namaKucing.extend(['Lalala', 'Meow'])
print(namaKucing)

# Menghapus list
# list.remove() = Menghapus elemen list 
namaKucing.remove('Kitty')
print(namaKucing)

# list.pop() = Menghapus elemen list berdasaarkan index tidak tau isi dan tipenya
namaKucing.pop(1)
print(namaKucing)

# del list = Menghapus list
del namaKucing[3]
print(namaKucing)

# list.clear() = Menghapus semua elemen list
namaKucing.clear()  # Menghapus semua elemen list tapi tetap ada listnya
print(namaKucing)



# Tuple =====================================================================================================
# Tuple adalah tipe data yang mirip dengan list, namun berbeda dengan list, tuple bersifat immutable yang berarti isi tuple tidak bisa diubah/diupdate
# Tuple menggunakan kurung biasa () atau kurung siku []
# Tupple tidak bisa diubah, dihapus, atau ditambahkan elemen baru


# Dictionary =====================================================================================================
# Dictionary adalah tipe data yang berisi pasangan key-value
# Dictionary menggunakan kurung kurawal {}
# Setiap key dipisahkan dari value-nya oleh titik dua (:) dan setiap pasangan key-value dipisahkan oleh koma (,)
# Key harus unik, jika terdapat dua key yang sama maka yang akan diambil adalah key yang terakhir

nama = {
            'nama' : 'Andi',
            'umur' : '24 tahun',
            'alamat' : 'Bengkulu',
            'hobi' : ['membaca', 'berenang']
        }

print(nama['nama'], nama['umur'], nama['alamat'], nama['hobi'][0], nama['hobi'][1])
            




















