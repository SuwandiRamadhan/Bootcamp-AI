# Fucntion non parameter
def halloDunia():
    var = f"Hallo Python, Hallo Dunia"
    print(var)
    
halloDunia()


# Function with parameter
def selamatDatang(nama, asal):
    var = f'Selamat datang {nama} dari {asal}'
    print(var)
    
selamatDatang("Andi", "Bengkulu")



# Buat function yang akan diisi dengan paramerter yang jumlahnya tidak tertentu
def selamatDatang(*daftarNama):   # Jika kita buat parameter dengan tanda * maka parameter tersebut akan dianggap sebagai tuple
    var = f'Hallo '
    for nama in daftarNama:
        var += nama + ', '
        
    var += 'Selamat datang!'
    print(var)

selamatDatang("Andi", "Budi", "Caca", "Deni", "Euis")


# Fungsi anonim atau lambda
# Fungsi lambda adalah fungsi anonim yang didefinisikan tanpa nama
fungsiAnonim = lambda x: x*2

print(fungsiAnonim(10))


# Comment dalam function
# Kita bisa akses komen multiline di function dengan memanggilnya di paramater dengan .__doc__

def penjumlahan(x, y):
    '''
    Fungsi ini digunakan untuk menjumlahkan dua bilangan
    bilangan pertama adalah x
    bilangan kedua adalah y
    '''
    hasil = x + y
    print(hasil)

penjumlahan(10, 20)
print(penjumlahan.__doc__)


# Return dan Scope
def operasiHitung(x, y):
    hasil = x + y
    return hasil

hasil = operasiHitung(5, 2)
print(hasil)
















